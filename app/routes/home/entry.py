from flask import Blueprint, render_template

from app.models.entry import Entry
h_entry = Blueprint('h_entry', __name__, url_prefix='/entry')

@h_entry.route('/')
@h_entry.route('/index')
def index():
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    return render_template('home/entry/index.html', title = 'All Entries', entries = entries)

@h_entry.route('/<string:slug>')
def show(slug):
    entry = Entry.query.filter_by(slug = slug).first_or_404()
    return render_template('home/entry/show.html', title = 'Test', entry = entry)
