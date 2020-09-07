from flask import Blueprint, render_template

from app.models.entry import Entry

h_main = Blueprint('h_main', __name__, url_prefix='/')

@h_main.route('/')
@h_main.route('/index')
def index():
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    return render_template('home/main/index.html', title = '/', entries = entries)

@h_main.route('/contact', methods = ['GET', 'POST'])
def contact():
    return render_template('home/main/contact.html', title = 'Contact')
