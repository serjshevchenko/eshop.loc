from flask.ext.sqlalchemy import SQLAlchemy
from eshop import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:%s/%s' % (app.config['DB_USERNAME'],
                                                                         app.config['DB_PASSWORD'],
                                                                         app.config['DB_HOST'],
                                                                         app.config['DB_PORT'],
                                                                         app.config['DB_NAME'])
db = SQLAlchemy(app)


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    url = db.Column(db.String(100), nullable=False, unique=True)
    text = db.Column(db.Text, nullable=False)

    def __init__(self, url, text):
        self.url = url
        self.text = text

    def __repr__(self):
        return '<Content by ling %s>' % self.url