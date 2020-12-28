# Forg

Frog is a flask based simple blog application.

<img src="https://i.imgyukle.com/2020/12/28/aalG71.png">

## Installation
Installation requires Python3 and Virtualenv.

```bash
~$ git clone https://github.com/emregeldegul/frog.git && cd frog
~$ python3 -m virtualenv venv
~$ source venv/bin/activate
~$ pip install -r requirements.txt
~$ flask db upgrade
~$ cp .env.example .env
```

Later, edit the .env file.

```bash
~$ nano .env

SITE_URL        = "127.0.0.1:5000"
SITE_NAME       = "Forg Blog"
SITE_TITLE      = "Forg Blog"
SITE_DESC       = "Flask Based Blog App"
SITE_SIGNATURE  = "Crazy Forg!"
SITE_TWITTER    = "emregeldegul"
SITE_GITHUB     = "emregeldegul"
```

You can now create a user.

```bash
~$ flask shell
>>> from app import db
>>> from app.models.user import User
>>> user = User(email='saknussemm@mail.com', name='Arne Saknussemm')
>>> user.generate_password_hash('journeyToCenterOfEarth')
>>> db.session.add(user)
>>> db.session.commit()
>>> exit()
```

You can now run the project.

```bash
~$ flask run
```
You can now visit http://localhost:5000. Your site is ready :)

## To Do

- [ ] Editing Profile / Password

## Used Technologies

* [flask] - Micro web framework
* [flask-sqlalchemy] - An extension for Flask that adds support for SQLAlchemy to your application.
* [flask-bcrypt] - Flask extension that provides bcrypt hashing utilities for your application.
* [flask-login] - Provides user session management for Flask.
* [flask-wtf] - Simple integration of Flask and WTForms, including CSRF, file upload, and reCAPTCHA.
* [flask-migrate] - Flask-Migrate is an extension that handles SQLAlchemy database migrations for Flask applications using Alembic.
## License

MIT

[flask]: <http://flask.pocoo.org>
[flask-sqlalchemy]: <https://flask-sqlalchemy.palletsprojects.com/en/2.x>
[flask-bcrypt]: <https://flask-bcrypt.readthedocs.io/en/latest>
[flask-login]: <https://flask-login.readthedocs.io/en/latest>
[flask-wtf]: <https://flask-wtf.readthedocs.io/en/stable>
[bootstrap]: <https://getbootstrap.com/>
[datatables]: <https://datatables.net/>
[flask-migrate]: <https://flask-migrate.readthedocs.io/en/latest/>
