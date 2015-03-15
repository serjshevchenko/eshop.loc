from eshop import db
from flask import url_for

class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<News %s>' % self.name


def get_list(page=1):
    news = News.query.all()
    for item in news:
        setattr(item, 'url', url_for('.show', name=item.name, id=item.id))
    return news


def get_show(id):
    return News.query.filter_by(id=id).first_or_404()