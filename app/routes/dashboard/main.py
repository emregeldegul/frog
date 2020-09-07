from os import environ

from flask import Blueprint, render_template
from app.forms.dashboard.main import SettingsForm

d_main = Blueprint('d_main', __name__, url_prefix='/dashboard')

@d_main.route('/')
@d_main.route('/index', methods = ['GET', 'POST'])
def index():
    form = SettingsForm()

    if form.validate_on_submit():
        environ['SITE_URL'] = form.url.data
        environ['SITE_NAME'] = form.name.data
        environ['SITE_TITLE'] = form.title.data
        environ['SITE_DESC'] = form.desc.data
        environ['SITE_SIGNATURE'] = form.signature.data
        environ['SITE_TWITTER'] = form.twitter.data
        environ['SITE_GITHUB'] = form.github.data

    form.url.data = environ['SITE_URL']
    form.name.data = environ['SITE_NAME']
    form.title.data = environ['SITE_TITLE']
    form.desc.data = environ['SITE_DESC']
    form.signature.data = environ['SITE_SIGNATURE']
    form.twitter.data = environ['SITE_TWITTER']
    form.github.data = environ['SITE_GITHUB']

    return render_template('dashboard/main/index.html', title = 'Dashboard', form = form)
