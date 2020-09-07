from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class CreateForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()], render_kw = {'placeholder': 'Title:', 'autocomplete': 'off'})
    slug = StringField('Slug', validators = [DataRequired()], render_kw = {'placeholder': 'Slug:', 'autocomplete': 'off'})
    content = TextAreaField('Content', validators = [DataRequired()], render_kw = {'placeholder': 'Content:', 'autocomplete': 'off', 'rows': '10'})
    #is_active = StringField('Sıte DESC', validators = [DataRequired()], render_kw = {'placeholder': 'Desc:', 'autocomplete': 'off'})
    submit = SubmitField('[ submit ]')


class EditForm(FlaskForm):
    title = StringField('Title', validators = [DataRequired()], render_kw = {'placeholder': 'Title:', 'autocomplete': 'off'})
    slug = StringField('Slug', validators = [DataRequired()], render_kw = {'placeholder': 'Slug:', 'autocomplete': 'off'})
    content = TextAreaField('Content', validators = [DataRequired()], render_kw = {'placeholder': 'Content:', 'autocomplete': 'off', 'rows': '10'})
    #is_active = StringField('Sıte DESC', validators = [DataRequired()], render_kw = {'placeholder': 'Desc:', 'autocomplete': 'off'})
    submit = SubmitField('[ submit ]')
