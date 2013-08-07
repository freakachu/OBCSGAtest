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
import datetime

#import pycrypto

from apiclient.discovery import build
from google.appengine.api import memcache
from src.config import OAuth2Handler

TimeStamp=datetime.datetime.now() - datetime.timedelta(hours=4)
logging.info(str(TimeStamp))

credentials = OAuth2Handler("fusiontables")

fusionTables = build("fusiontables", "v1", http=credentials)
tableID='1FldbAM9tCWQxWAm1MqOBYI6NsXl4IZQbYuAtjCg'

class ftclient():
    
    def __init__(self):

        self.columns = ['TimeStamp','First Name', 'Last Name', 'Email Address', 'Taking OBC 301', 'Date of Class',
                        'Prophecy', 'Serving', 'Teaching', 'Exhortation', 'Giving', 'Administration', 'Mercy']
        self.values = [TimeStamp]
    
    def name(self,first,last):
        self.values.append(first)
        self.values.append(last)

    def email(self,email):
        self.values.append(email)
        
    def classCheck(self, attend, DoC):
        if  attend == True:
            self.values.append('Yes')
            self.values.append(DoC)
        else:
            self.values.append("No")
            self.values.append("N/A")
    
    def scoreInput(self,score):
        self.values.append(score)

    def updateTable(self):
         
        print self.columns.values()
        print self.values.values()
        
        
        self.response = fusionTables.query().sql(sql="insert into "+tableID+ "(" + str(self.columns) + ')' + 'values (' + str(self.values) +')').execute(http=credentials)
        


if __name__ == '__ftclient__':
    ftclient()