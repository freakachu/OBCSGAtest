import os

"Project Director"
PROJECT_DIR = os.getcwd()[0]
"Project Sub-Directories"
STATICFILES_DIR = os.path.join(PROJECT_DIR,'static')
TEMPLATES_DIR = os.path.join(PROJECT_DIR,'templates')
HELPERS_DIR = os.path.join(PROJECT_DIR,'helpers')
LIB_DIR = os.path.join(PROJECT_DIR,'lib')
SRC_DIR = os.path.join(PROJECT_DIR,'src')

"Lib Sub Packages Paths"
APICLIENT = os.path.join(LIB_DIR,'apiclient')
HTTPLIB2 = os.path.join(LIB_DIR,'httblib2')
MEMCACHE = os.path.join(LIB_DIR,'memcache')
OAUTH2 = os.path.join(LIB_DIR,'oauth2client')
URITMP = os.path.join(LIB_DIR,'uritemplate')
"Static Files Folder Paths"
IMG_DIR = os.path.join(STATICFILES_DIR,'img')
"Templates Folder Paths"
HTML_DIR = os.path.join(TEMPLATES_DIR, 'html')
CSS_DIR = os.path.join(TEMPLATES_DIR,'css')
IMGS_DIR = os.path.join(TEMPLATES_DIR,'img')