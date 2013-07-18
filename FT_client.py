'''
Created on Jul 16, 2013

@author: jlambright
'''

import httplib2
import logging
import os
import pickle
import datetime

"""
The following imports are for OAuth2 & Google API interation. This shoud allow us to use the built-in method found in:
  
  Fusion Tables: https://google-api-client-libraries.appspot.com/documentation/fusiontables/v1/python/lates/index.html
  
  OAuth2Client: https://google-api-python-client.googlecode.com/hg/docs/epy/oauth2client-module.html

"""

from apiclient.discovery import build
from oauth2client.appengine import AppAssertionCredentials
from oauth2client.client import SignedJwtAssertionCredentials
from google.appengine.api import memcache
from google.appengine.ext import webapp
from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app








if __name__ == '__main__':
    pass