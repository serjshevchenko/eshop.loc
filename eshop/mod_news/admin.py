from flask.ext.admin.contrib.sqla import ModelView

from .models import News


class NewsView(ModelView):
    edit_template = 'admin/news/edit.html'
    create_template = 'admin/news/create.html'

    form_widget_args = dict(
        text={'class': 'textarea-jqte'}
    )

    def __init__(self, session, **kwargs):
        super(NewsView, self).__init__(News, session, endpoint='admin.news', url='news', **kwargs)

