from eshop import db


class News(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(250), nullable=False)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<News %s>' % self.name