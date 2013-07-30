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
        self.giftScores = {
                           'Category':['Prophecy', 'Serving', 'Teaching', 'Exhortation', 'Giving', 'Administration', 'Mercy'],
                           'Score':[0,0,0,0,0,0,0]
                           }
        self.dict = {}
        self.dict["TimeStamp"] = TimeStamp
    
    def name(self,first,last):
        self.dict['First Name'] = first
        self.dict['Last Name'] = last

    def email(self,email):
        self.dict["Email Address"] = email
        
    def classCheck(self, attend, DoC):
        if  attend == True:
            self.dict["Taking OBC 301"] = "Yes"
            self.dict["Date of Class"]  = DoC
        else:
            self.dict["Taking OBC 301"] = "No"
            self.dict["Date of Class"]  = "N/A"
    
    def scoreInput(self,scores):
        self.giftScores['Scores'] = scores.copy()

    def updateTable(self):
        self.response = fusionTables.query().sql(sql="insert into "+tableID+ "(" + str(self.dict.key() + self.giftScores.keys()) +")" +
                                             "values ('"+ str(self.dict.values()) + str(self.giftScores.values()) +')').execute(http=credentials)
        


if __name__ == '__ftclient__':
    ftclient()