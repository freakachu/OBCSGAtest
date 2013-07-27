import os
PROJECT_DIR = os.path.realpath(os.path.dirname(__file__))
STATIC_ROOT = '/OBCSGatest/static/'
STATIC_URL = ' /static/'
STATICFILES_DIR = os.path.join(PROJECT_DIR+'/static',)
TEMPLATES_DIR = os.path.join(PROJECT_DIR+'/templates/',)
HTML_DIR = os.path.join(TEMPLATES_DIR, 'html')
CSS_DIR = os.path.join(TEMPLATES_DIR+'/css',)
IMGS_DIR = os.path.join(TEMPLATES_DIR+'/img',)