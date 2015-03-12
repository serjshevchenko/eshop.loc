import os

_cwd = os.path.dirname(os.path.abspath(__file__))

MENU_CONF_FILENAME = os.path.join(_cwd, 'top-menu.json')
LOG_FILE = os.path.join(_cwd, 'log', 'app.log')
SECRET_KEY = 'some hidden key'
DEBUG = True
# database
DB_NAME = 'eshop'
DB_HOST = 'localhost'
DB_PORT = '5432'
DB_USERNAME = 'eshop'
DB_PASSWORD = 'admin'