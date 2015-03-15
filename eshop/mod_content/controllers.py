from flask import Blueprint, render_template, url_for
from flask.ext import menu
from .models import Content, get_content
from .admin import ContenView

content_bp = Blueprint('content', __name__)


@content_bp.route('/')
@menu.register_menu(content_bp, '.home', 'Home',
                    dynamic_list_constructor=lambda: dict(icon='icon-home'),
                    order=0)
def home():
    text = get_content('/home.html')
    return render_template('content/home.html', text=text)


@content_bp.route('/about.html')
@menu.register_menu(content_bp, '.about', 'About',
                    dynamic_list_constructor=lambda: dict(icon='icon-info-circled'),
                    order=1)
def about():
    text = get_content(url_for('.about'))
    return render_template('content/about.html', text=text)


@content_bp.route('/contact.html')
@menu.register_menu(content_bp, '.contact', 'Contact',
                    dynamic_list_constructor=lambda: dict(icon='icon-mail'),
                    order=2)
def contact():
    text = get_content(url_for('.contact'))
    return render_template('content/contact.html', text=text)

