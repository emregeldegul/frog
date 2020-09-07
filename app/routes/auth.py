from flask import Blueprint, redirect, url_for, render_template, flash
from flask_login import logout_user, current_user, login_user

from app.models.user import User
from app.forms.auth import LoginForm

auth = Blueprint('auth', __name__, url_prefix='/auth')

@auth.route('/')
@auth.route('/index')
def index():
    return redirect(url_for('auth.login'))

@auth.route('/register')
def register():
    return 'ok'

@auth.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('d_main.index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()

        if user is None or not user.check_password(form.password.data):
            flash('Login Failed')
        else:
            login_user(user)
            redirect(url_for('d_main.index'))

    return render_template('auth/login.html', title = 'Login', form = form)

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
