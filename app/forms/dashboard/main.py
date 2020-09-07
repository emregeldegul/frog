from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class SettingsForm(FlaskForm):
    url = StringField('Sıte URL', validators = [DataRequired()], render_kw = {'placeholder': 'URL:', 'autocomplete': 'off'})
    name = StringField('Sıte Name', validators = [DataRequired()], render_kw = {'placeholder': 'Name:', 'autocomplete': 'off'})
    title = StringField('Sıte Title', validators = [DataRequired()], render_kw = {'placeholder': 'Title:', 'autocomplete': 'off'})
    desc = StringField('Sıte DESC', validators = [DataRequired()], render_kw = {'placeholder': 'Desc:', 'autocomplete': 'off'})
    signature = StringField('Sıte Signature', validators = [DataRequired()], render_kw = {'placeholder': 'Signature:', 'autocomplete': 'off'})
    twitter = StringField('Sıte Twitter', validators = [DataRequired()], render_kw = {'placeholder': 'Twitter:', 'autocomplete': 'off'})
    github = StringField('Sıte GitHub', validators = [DataRequired()], render_kw = {'placeholder': 'GitHub:', 'autocomplete': 'off'})
    submit = SubmitField('[ submit ]')
