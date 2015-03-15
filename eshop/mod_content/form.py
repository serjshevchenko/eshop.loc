from flask.ext.admin import form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Regexp


class ContentForm(form.BaseForm):
    url = StringField('Url', validators=[
                                         Regexp("\d+", message='Must satisfy the pattern "/<name>.html"')])
    text = TextAreaField('Text', [DataRequired()])