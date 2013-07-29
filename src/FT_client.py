#!/usr/bin/env python
#
# Copyright 2012 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Starting template for Google App Engine applications.

Use this project as a starting point if you are just beginning to build a Google
App Engine project. Remember to download the OAuth 2.0 client secrets which can
be obtained from the Developer Console <https://code.google.com/apis/console/>
and save them as 'client_secrets.json' in the project Pathectory.
"""

import logging
import os
import sys
import pickle
import webapp2



import httplib2
from apiclient.discovery import build
from oauth2client.client import AccessTokenRefreshError
from google.appengine.api import memcache
from oauth2client.client import SignedJwtAssertionCredentials



f=file('static/key.pem', 'rb')
key= f.read()
f.close()

credentials= SignedJwtAssertionCredentials(
            '642636158554@developer.gserviceaccount.com',
            key,
            scope='https://www.googleapis.com/auth/fusiontables')


http = httplib2.Http(memcache)
http = credentials.authorize(http)
service = build("fusiontables", "v1", http=http)




class MainHandler(webapp2.RequestHandler):

    
    def get(self):
        self.response.write(str(credentials))
        tables=service.table().list().execute(http)
        self.response.write(str(tables))

def main():
    application = webapp2.WSGIApplication(
      [
       ('/FTtest', MainHandler)
      ],
      debug=True)
    application.run()


if __name__ == '__main__':
    main()