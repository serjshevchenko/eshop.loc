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

#app.secret_key = 'some_secret'
app.logger.addHandler(handler)

import eshop.view

# db.create_all()
