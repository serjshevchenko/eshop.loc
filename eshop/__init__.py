#!/usr/bin/python
from flask import Flask
import logging
import json
import logging.handlers
from flask.ext import menu

app = Flask(__name__)
menu.Menu(app=app)
app.config.from_object('config')

handler = logging.handlers.RotatingFileHandler(app.config['LOG_FILE'], maxBytes=1048576, backupCount=3)
handler.setLevel(logging.INFO if not app.config['DEBUG'] else logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

navigation_bar = list()
# with open(app.config['MENU_CONF_FILENAME'], 'rt') as file:
#     navigation_bar = json.load(file)


#app.secret_key = 'some_secret'
app.logger.addHandler(handler)
app.jinja_env.globals.update(navigation_bar=navigation_bar)

app.logger.debug(navigation_bar)

import eshop.view

# db.create_all()
