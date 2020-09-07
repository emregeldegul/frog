from flask import Blueprint, render_template

from app.models.page import Page

h_page = Blueprint('h_page', __name__, url_prefix='/page')

@h_page.route('/')
@h_page.route('/index')
def index():
    return render_template('home/page/index.html')

@h_page.route('/<string:slug>')
def show(slug):
    page = Page.query.filter_by(slug = slug).first_or_404()
    return render_template('home/page/show.html', title = page.title, page = page)
