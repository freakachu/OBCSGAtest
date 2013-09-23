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

"""
Connects to, and updates, the Google Fusion Tables document, 
for results data analysis and storage.

"""


import logging
import os
import sys
import pickle
import webapp2
import datetime
import time

#import pycrypto
from collections import OrderedDict
from pytz.gae import pytz
from apiclient.discovery import build
from google.appengine.api import memcache
from src.config import OAuth2Handler

eastern=pytz.timezone('US/Eastern')
TimeStamp=datetime.datetime.now(eastern)
logging.info(str(TimeStamp))

credentials = OAuth2Handler("fusiontables")

fusionTables = build("fusiontables", "v1", http=credentials)
tableID='1FldbAM9tCWQxWAm1MqOBYI6NsXl4IZQbYuAtjCg'

class ftclient():
    
    def __init__(self):
        
        self.dict = OrderedDict()
        self.dict["TimeStamp"]=str(TimeStamp)
        
    
    def name(self,first,last):
        self.dict["First Name"]=first
        self.dict["Last Name"]=last

    def email(self,email):
        self.dict["Email Address"]=email
        
    def classCheck(self, attend, DoC):
        if  attend == True:
            self.dict["Taking OBC 301"]='Yes'
            self.dict["Date of Class"]=DoC
        else:
            self.dict["Taking OBC 301"]='No'
            self.dict["Date Of Class"]='N/A'

    def updateTable(self,od):
        for k in od:
            self.dict[k]=od[k]['score']
        
        #logging.info(self.dict)
        columns = str(tuple(self.dict.keys()))
        values = str(tuple(self.dict.values()))
        #logging.info("************************\n**************************\n")
        #there. NOW this statement is valid SQL.
        sqlStr = 'insert into %s %s values%s' % (tableID, columns, values)
        #logging.info(sqlStr)
        self.response = fusionTables.query().sql(sql=sqlStr).execute(http=credentials)
        


if __name__ == '__ftclient__':
    ftclient()