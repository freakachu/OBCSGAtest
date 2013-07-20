'''
Created on Jul 19, 2013

@author: jlambright

This will direct calls to our client/helper classes, and templates.

Need to figure out how to route the calls to sgtest.py and FT_client.py . 

'''
import os

from gae.lib.webapp2 import webapp2
from src.main import FT_client, sgtest
from src.main.sgtest import MainPage
from src.main.FT_client import FTHandler

class MainPage(webapp2.RedirectHandler):
       def get(self):
           {
        # Models are queried here, results transferred to template_values

      
            }
           path = os.path.join(os.path.dirname(__file__), 'sgtest.py')
           self.response.out.write(template.render(path, template_values))
           
class FTHandler(webapp2.RedirectHandler):
       def get(self):
           {
        # Models are queried here, results transferred to template_values

      
            }

           path = os.path.join(os.path.dirname(__file__), 'FT_client.py')
           self.response.out.write(template.render(path, template_values))
if __name__ == '__main__':
    pass