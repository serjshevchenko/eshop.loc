from flask import Blueprint, render_template
from flask.ext import menu
from .models import Content
from .admin import ContenView

content_bp = Blueprint('content', __name__)


@content_bp.route('/')
@menu.register_menu(content_bp, '.home', 'Home',
                    dynamic_list_constructor=lambda: dict(icon='icon-home'),
                    order=0)
def home():
    return render_template('content/home.html')


@content_bp.route('/about')
@menu.register_menu(content_bp, '.about', 'About',
                    dynamic_list_constructor=lambda: dict(icon='icon-info-circled'),
                    order=1)
def about():
    return render_template('content/about.html')


@content_bp.route('/contact')
@menu.register_menu(content_bp, '.contact', 'Contact',
                    dynamic_list_constructor=lambda: dict(icon='icon-mail'),
                    order=2)
def contact():
    return render_template('content/contact.html')

