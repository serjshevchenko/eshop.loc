from flask import render_template, request
from eshop import app, menu
# from eshop.orm import Content, db


@app.route('/')
@menu.register_menu(app, '.home', 'Home',
                    active_when=lambda: request.endpoint == 'home',
                    dynamic_list_constructor=lambda: dict(icon='icon-home'),
                    order=0)
def home():
    template_vars = {
    }
    # c = Content(url='/', text='<p><b>Text For Home PAGE</b></p>')
    # app.logger.warning(dir(request))
    # import pdb; pdb.set_trace()
    # db.session.add(c)
    # db.session.commit()
    return render_template('home.html', **template_vars)


@app.route('/news', defaults={'page': 1})
@app.route('/news/<page>')
@menu.register_menu(app, '.news', 'News',
                    active_when=lambda: request.endpoint == 'news',
                    dynamic_list_constructor=lambda: dict(icon='icon-newspaper'),
                    order=1)
def news(page):
    template_vars = {
        'page': page
    }
    # import pdb; pdb.set_trace()
    return render_template('news.html', **template_vars)


@app.route('/about')
@menu.register_menu(app, '.about', 'About',
                    active_when=lambda: request.endpoint == 'about',
                    dynamic_list_constructor=lambda: dict(icon='icon-info-circled'),
                    order=2)
def about():
    template_vars = {
    }
    return render_template('about.html', **template_vars)


@app.route('/contact')
@menu.register_menu(app, '.contact', 'Contact',
                    active_when=lambda: request.endpoint == 'contact',
                    dynamic_list_constructor=lambda: dict(icon='icon-mail'),
                    order=3)
def contact():
    template_vars = {
    }
    return render_template('contact.html', **template_vars)


@app.route('/user')
def user():
    return render_template('user.html')


@app.route('/administration')
@menu.register_menu(app, '.admin', 'Administration',
                    active_when=lambda: request.endpoint == 'admin',
                    dynamic_list_constructor=lambda: dict(icon='icon-edit'),
                    order=4)
def admin():
    # navigation_bar
    return render_template('admin.html')



# @app.route('/catalog', defaults={'name': None, 'page': None})
# @app.route('/catalog/<name>', defaults={'page': 1})
# @app.route('/catalog/<name>/<page>')
# def catalog(name, page):
#     if name is None:
#         render = lambda: render_template('catalog_menu.html')
#     else:
#         render = lambda: render_template('catalog_type.html', name=name, page=page)
#     return render()
