'''
Created on Jul 16, 2013

@author: joshua.lambright@gmail.com
'''


import os
import datetime
import webapp2

"""
The following imports are for OAuth2 & Google API interaction. This should allow us to use the built-in method found in:
  
  Fusion Tables: https://google-api-client-libraries.appspot.com/documentation/fusiontables/v1/python/lates/index.html
  
  OAuth2Client: https://google-api-python-client.googlecode.com/hg/docs/epy/oauth2client-module.html

"""

from apiclient.discovery import build

from oauth2client.appengine import logging, memcache, pickle, httplib2, AppAssertionCredentials, OAuth2DecoratorFromClientSecrets
from oauth2client.client import AccessTokenCredentials

from google.appengine.api import urlfetch

from google.appengine.ext.webapp import template
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import remote_api

from webapp2_extras import jinja2


# CLIENT_SECRETS, name of a file containing the OAuth 2.0 information for this
# application, including client_id and client_secret.
# You can see the Client ID and Client secret on the API Access tab on the
# Google APIs Console <https://code.google.com/apis/console>
CLIENT_SECRETS = os.path.join(os.path.dirname(__file__), 'client_secrets.json')

# Helpful message to display in the browser if the CLIENT_SECRETS file
# is missing.
MISSING_CLIENT_SECRETS_MESSAGE = """
<h1>Warning: Please configure OAuth 2.0</h1>
<p>
To make this sample run you will need to populate the client_secrets.json file
found at:
</p>
<code>%s</code>
<p>You can find the Client ID and Client secret values
on the API Access tab in the <a
href="https://code.google.com/apis/console">APIs Console</a>.
</p>

""" % CLIENT_SECRETS


http = httplib2.Http(memcache)
service = build("fusiontables", "v1", http=http)


# Set up an OAuth2Decorator object to be used for authentication.  Add one or
# more of the following scopes in the scopes parameter below. PLEASE ONLY ADD
# THE SCOPES YOU NEED. For more information on using scopes please see
# <https://developers.google.com/+/best-practices>.
decorator = oauth2decorator_from_clientsecrets(
    CLIENT_SECRETS,
    scope=[
      'https://www.googleapis.com/auth/fusiontables',
      'https://www.googleapis.com/auth/fusiontables.readonly',
    ],
    message=MISSING_CLIENT_SECRETS_MESSAGE)

class MainHandler(webapp2.RequestHandler):

  @decorator.oauth_required
  def get(self):
    self.response.out.write("""<html><body>

  <p>Congratulations, you are up and running! At this point you will want to add
  calls into the Fusion Tables API to the <code>main.py</code> file. Please read the
  <code>main.py</code> file carefully, it contains detailed information in
  the comments.  For more information on the Fusion Tables API Python library
  surface you can visit: </p>

 <blockquote>
   <p>
   <a href="https://google-api-client-libraries.appspot.com/documentation/fusiontables/v1/python/latest/">
   https://google-api-client-libraries.appspot.com/documentation/fusiontables/v1/python/latest/
   </a>
   </p>
 </blockquote>

  <p>
  Also check out the <a
    href="https://developers.google.com/api-client-library/python/start/get_started">
    Python Client Library documentation</a>, and get more information on the
  Fusion Tables API at:
  </p>

  <blockquote>
    <p>
    <a href="https://developers.google.com/fusiontables">https://developers.google.com/fusiontables</a>
    </p>
  </blockquote>
""")

def main():
  application = webapp2.WSGIApplication(
      [
       ('/', MainHandler),
       (decorator.callback_path, decorator.callback_handler()),
      ],
      debug=True)
  run_wsgi_app(application)


if __name__ == '__main__':
  main()
