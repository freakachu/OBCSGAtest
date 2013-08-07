import logging
import os
import httplib2
from google.appengine.api import memcache
from oauth2client.client import SignedJwtAssertionCredentials


#Project path variables.

"App Engine Path"
APP_ENGINE_PATH='../../google_appengine'

"Main Project Pathectory '/' "
PROJECT_Path = os.getcwd()

API_Path = os.path.join(PROJECT_Path, 'apiclient')
HTTPLIB2_Path = os.path.join(PROJECT_Path,'httplib2')
OAUTH2_Path = os.path.join(PROJECT_Path,'oath2client')
URITMPL8_Path = os.path.join(PROJECT_Path,'uritemplate')

"Source Package '/src'"
SRC_Path = os.path.join(PROJECT_Path, 'src')

"Helpers Package /helpers"
HLP_Path = os.path.join(PROJECT_Path, 'helpers')

"Static Files Folder '/static'"
STATICFILES_Path = os.path.join(PROJECT_Path, 'static')
"It's Sub-Pathectories:"
IMGS_Path = os.path.join(STATICFILES_Path,'img')

"Template Files Package '/templates'"
TEMPLATES_Path = os.path.join(PROJECT_Path,'templates')
"It's Sub-Pathectories:"
HTML_Path = os.path.join(TEMPLATES_Path, 'html')
CSS_Path = os.path.join(TEMPLATES_Path,'css')


#Global method for OAuth2 Service authentication.
def OAuth2Handler(text):
        apiName = text
        http = httplib2.Http(memcache)
        f=file('key.pem', 'rb')
        key= f.read()
        f.close() 
        creds = SignedJwtAssertionCredentials('642636158554@developer.gserviceaccount.com',key,
                              scope=('https://www.googleapis.com/auth/'+ apiName))
            
        http = creds.authorize(http)
        return http

