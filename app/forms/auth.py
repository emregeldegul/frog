from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField('E-Mail', validators = [DataRequired(), Email()], render_kw = {'placeholder': 'email:', 'autocomplete': 'off', 'value': 'email:'})
    password = PasswordField('Password', validators = [DataRequired()], render_kw = {'placeholder': 'password:', 'autocomplete': 'off', 'value': 'password:'})
    submit = SubmitField('[ submit ]')
