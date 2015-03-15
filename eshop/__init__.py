#!/usr/bin/python
import logging
import logging.handlers

from flask import Flask
from flask.ext import menu
from flask.ext.admin import Admin
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')


menu.Menu(app=app)


handler = logging.handlers.RotatingFileHandler(app.config['LOG_FILE'], maxBytes=1048576, backupCount=3)
handler.setLevel(logging.INFO if not app.config['DEBUG'] else logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

app.logger.addHandler(handler)


db = SQLAlchemy(app)

# db.create_all()


from eshop.mod_content import controllers as content_module
from eshop.mod_news import controllers as news_module


app.register_blueprint(content_module.content_bp)
app.register_blueprint(news_module.news_bp)


admin = Admin(app, endpoint='admin')
admin.add_view(news_module.NewsView(db.session))
admin.add_view(content_module.ContenView(db.session))