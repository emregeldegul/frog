from flask import Blueprint, render_template, flash
from flask_login import login_required

from app import db
from app.models.entry import Entry
from app.forms.dashboard.entry import CreateForm, EditForm

d_entry = Blueprint('d_entry', __name__,  url_prefix='/dashboard/entry')

@login_required
@d_entry.route('/')
@d_entry.route('/index')
def index():
    entries = Entry.query.order_by(Entry.created_at.desc()).all()
    return render_template('dashboard/entry/index.html', title = 'Entries', entries = entries)

@login_required
@d_entry.route('/create', methods = ['GET', 'POST'])
def create():
    form = CreateForm()

    if form.validate_on_submit():
        entry = Entry(
            title = form.title.data,
            slug = form.slug.data,
            content = form.content.data
        )

        db.session.add(entry)
        db.session.commit()

        flash('Added Successful')

    return render_template('dashboard/entry/create.html', title = 'Create', form = form)

@login_required
@d_entry.route('/<string:slug>')
def show():
    return 'ok'


@login_required
@d_entry.route('/<string:slug>/edit', methods = ['GET', 'POST'])
def edit(slug):
    entry = Entry.query.filter_by(slug = slug).first_or_404()

    form = EditForm()

    if form.validate_on_submit():
        entry.title = form.title.data
        entry.slug = form.slug.data
        entry.content = form.content.data

        db.session.commit()

        flash('Update Successful')

    form.title.data = entry.title
    form.slug.data = entry.slug
    form.content.data = entry.content

    return render_template('dashboard/entry/edit.html', title = entry.title + 'Edit', entry = entry, form = form)
