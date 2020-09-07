from flask import Blueprint, render_template, flash
from flask_login import login_required

from app import db
from app.models.page import Page

d_page = Blueprint('d_page', __name__,  url_prefix='/dashboard/page')

@login_required
@d_page.route('/')
@d_page.route('/index')
def index():
    return 'ok'

@login_required
@d_page.route('/create', methods = ['GET', 'POST'])
def create():
    return 'ok'

@login_required
@d_page.route('/<string:slug>')
def show():
    return 'ok'


@login_required
@d_page.route('/<string:slug>/edit', methods = ['GET', 'POST'])
def edit(slug):
    return 'ok'
