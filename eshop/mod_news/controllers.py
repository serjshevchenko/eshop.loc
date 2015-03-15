from flask import Blueprint, render_template
from flask.ext import menu
from .models import News, get_list, get_show
from .admin import NewsView

news_bp = Blueprint('news', __name__, url_prefix='/news')


@news_bp.route('/', defaults={'page': 1})
@news_bp.route('/<int:page>')
@menu.register_menu(news_bp, '.news', 'News',
                    dynamic_list_constructor=lambda: dict(icon='icon-newspaper'),
                    order=3)
def list(page):
    loc_context = {
        'page': page,
        'news': get_list(page=page)
    }
    return render_template('news/list.html', **loc_context)


@news_bp.route('/<name>-<int:id>.html')
def show(name, id):
    loc_context = {
        'item': get_show(id)
    }
    return render_template('news/show.html', **loc_context)