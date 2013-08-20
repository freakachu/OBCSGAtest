import random
import webapp2
import sys
import httplib2
import jinja2
import logging

from src.FT_client import ftclient
from google.appengine.api import memcache
from collections import OrderedDict
from webapp2_extras import sessions

#config options for sessions
#secret_key has to be set to something in order for this to work at all
config = {}
config["webapp2_extras.sessions"] = {
    "secret_key": "nubcakery",
    "session_max_age": 432000 #5 days
}


#base handler class to setup sessions with webapp2
class BaseHandler(webapp2.RequestHandler):
    def dispatch(self):
        self.session_store = sessions.get_store(request=self.request)
        try:
            webapp2.RequestHandler.dispatch(self)
        finally:
            self.session_store.save_sessions(self.response)
    @webapp2.cached_property
    def session(self):
         #setup sessions using memcache backend instead of the secure cookie default
        return self.session_store.get_session(backend='memcache')

class MainPage(BaseHandler):
    
    
    def get(self):
        
        
        questions=[]     
        questionsOnPage=[]
        qFile= file("questions.txt", "r")
        for question in qFile:
            questions.append(question)
        qFile.close()
        
        page=1 #default to page 1
        questionsPerPage=10
        maxPages=len(questions)/questionsPerPage
        if(len(questions) % questionsPerPage > 0):
            #account for partial pages
            maxPages+=1
            
        orderOnPage=[]
        #if no session is setup, create initial data
        if(not self.session.get('order')):        
            #randomize question order in a way that we still know what's what
            order=range(len(questions))
            random.shuffle(order)
            self.session['order']=order
            self.session['page']=page
        else: #session exists, we may not be on the first page
            order=self.session.get('order')
            if(self.request.get('page')):
                page=int(self.request.get('page'))
                self.session['page']=page
            else:
                page=int(self.session.get('page'))
            #logging.info("session page is: %d" % page)
            
            
        #determine the start and ending indexes
        #ending index can't be greater than the length, obviously
        questionIndexStart=0
        questionIndexEnd=0
        questionIndexStart=questionsPerPage*(page-1)
        if((questionIndexStart)+(questionsPerPage)>len(questions)):
            questionIndexEnd=len(questions)
        else:
            questionIndexEnd=questionIndexStart+questionsPerPage
        
        for q in range(questionIndexStart, questionIndexEnd):
            questionsOnPage.append(questions[order[q]])
            orderOnPage.append(order[q])
        
        for parameter in self.request.arguments():
            self.session[parameter]=self.request.get(parameter)
        
        JINJA_ENVIRONMENT = jinja2.Environment(loader= jinja2.FileSystemLoader('templates/html'), autoescape=True)
        values={"questions": questionsOnPage, "order": orderOnPage, "pageNum": page, "questionsPerPage":questionsPerPage, "maxPages" : maxPages}
        template = JINJA_ENVIRONMENT.get_template('test_template.html')
        self.response.write(template.render(values))
        #TODO: paginate the questions!
        
class evaluator(BaseHandler):
    
    def post(self):
        
        #This dictionary contains the gift categories, their questions, and scores. 
        gifts = OrderedDict()
        gifts['Prophecy'] = {'questions':[5, 11, 15, 24, 26, 30, 37, 40, 46, 50, 61, 63, 67, 85, 90],'score':0}
        gifts['Service'] = {'questions':[1, 9,12, 19, 22, 28, 34, 39, 43, 53, 58, 62, 64, 80, 87],'score':0}
        gifts['Teaching'] = {'questions':[6, 17, 48, 57, 60, 74, 75, 77, 88, 89, 92, 94, 99, 101, 105],'score':0}
        gifts['Exhortation'] = {'questions':[3, 7, 13, 31, 36, 45, 51, 52, 70, 78, 79, 81, 83, 97, 103],'score':0}
        gifts['Giving'] = {'questions':[2, 10, 18, 25, 32, 41, 47, 55, 65, 69, 72, 76, 86, 98, 104],'score':0}
        gifts['Administration'] = {'questions':[8, 14, 20, 23, 29, 35, 44, 49, 56, 71, 73, 82, 93, 95, 102],'score':0}
        gifts['Mercy'] = {'questions':[4, 16, 21, 27, 33, 38, 42, 54, 59, 66, 68, 84, 91, 96],'score':0}
        
        giftList = gifts.keys()
        scores = list()
        ftc = ftclient()
        # for gift in gifts.iteritems():
        #     for x in gift[1]:
        #         if self.request.get("question"+str(x)):
        #             scores[gift[0]]+=int(self.request.get("question"+str(x)))
       
        #merge session and posted question answers
        for parameter in self.request.arguments():
            if("question" in parameter):
                self.session[parameter]=self.request.get(parameter)
         
                 
        for k in gifts:
            #Retrieves the question numbers from the dictionary associated with "k", where "k" is a key in gifts.
            giftQs = gifts.get(k).get('questions')
            #Retrieves the score value from the dictionary associated with "k", where "k" is a key in gifts.
            #score = gifts.get(k).get('score')
            for qnum in giftQs:
                logging.info("question"+str(qnum))
                logging.info(self.session.get("question"+str(qnum)))
                if self.session.get("question"+str(qnum)):
                    gifts[k]['score'] +=int(self.session.get("question"+str(qnum)))
            scores.append(gifts[k]['score'])   
        
        
        
        #these fields should be verified, specially the email.
        #we should probably do that with JS on the page itself
        #but doing it again here can't hurt
        firstName=self.session.get("firstName")
        lastName=self.session.get("lastName")
        email=self.session.get("email")
        attend=self.session.get("isTakingClass")
        DoC=self.session.get("classDate")
              
        ftc.name(firstName, lastName)
        ftc.email(email)
        ftc.classCheck(attend, DoC)
        ftc.updateTable(gifts)
        
        #time to render the results template
        jinjaEnv=jinja2.Environment(loader= jinja2.FileSystemLoader('templates/html'), autoescape=True)
        values={"giftNames": giftList, "scores": scores}
        template = jinjaEnv.get_template('result_template.html')
        self.response.write(template.render(values))
        
        #self.response.write(response)
        #we now have all the values as far as the main test is concerned.
        
        
        


application = webapp2.WSGIApplication([('/', MainPage), ('/submit', evaluator)], debug=True, config=config)

def main():
    application.run()

if __name__ == "__main__":
    main()