'''
Created on Jul 19, 2013

@author: jlambright

This will direct calls to our client/helper classes, and templates.

Need to figure out how to route the calls to sgtest.py and FT_client.py . 

'''
import os

from gae.lib.webapp2 import webapp2
#from main import FT_client, sgtest
from main.sgtest import MainPage, evaluator
from main.FT_client import FTHandler

           
#this right here is how you sort out what gets called when.
application = webapp2.WSGIApplication([('/', MainPage), ('/submit', evaluator), ('/FTtest', FTHandler)], debug=True)

def main():
    application.run()

if __name__ == '__main__':
    pass