import os

"""
pathectory: noun.
the horrible mangling of the words "path" and "dirctory" into a meaningless portmanteau.

see "URLdress"  
"""


"Main Project Pathectory '/' "
#'/' is the root directory on a unix filesystem.  that will almost never be the Current Working Directory.
#it's fixed now to actually work properly
#you're welcome.
PROJECT_Path = os.getcwd()

"Lib Package '/lib'"
LIB_Path = os.path.join(PROJECT_Path,'lib')
"It's Sub-Pathectories:"
API_Path = os.path.join(LIB_Path, 'apiclient')
HTTPLIB2_Path = os.path.join(LIB_Path,'httplib2')
OAUTH2_Path = os.path.join(LIB_Path,'oath2client')
URITMPL8_Path = os.path.join(LIB_Path,'uritemplate')

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


# Used to verify correct paths.
#print ('----------------' + '\n' + (PROJECT_Path + "\n" + STATICFILES_Path + "\n" + TEMPLATES_Path + "\n" + HTML_Path + "\n" + CSS_Path + "\n" + IMGS_Path + "\n" +HTTPLIB2_Path + "\n" +SRC_Path))