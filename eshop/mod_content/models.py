from eshop import db


class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    url = db.Column(db.String(100), nullable=False, unique=True)
    text = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return '<Content by ling %s>' % self.ur