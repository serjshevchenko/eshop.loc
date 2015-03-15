from flask.ext.admin.contrib.sqla import ModelView
from wtforms.validators import Regexp

from .models import Content


class ContenView(ModelView):
    edit_template = 'admin/content/edit.html'
    create_template = 'admin/content/create.html'

    form_args = dict(
        url=dict(label='Url', validators=[Regexp('^\/\w+\.html$', message='Must satisfy the pattern "/<name>.html"')]),
    )

    form_widget_args = dict(
        text={'class': 'textarea-jqte'}
    )

    def __init__(self, session, **kwargs):
        super(ContenView, self).__init__(Content, session, endpoint='admin.content', url='content', **kwargs)
