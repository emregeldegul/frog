from os import getenv

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.context_processor
    def context_processor():
        from app.models.page import Page
        header_pages = Page.query.filter_by(is_active = True).all()

        return dict(
            site_url = getenv('SITE_URL'),
            site_name = getenv('SITE_NAME'),
            site_title = getenv('SITE_TITLE'),
            site_desc = getenv('SITE_DESC'),
            site_signature = getenv('SITE_SIGNATURE'),
            site_twitter = getenv('SITE_TWITTER'),
            site_github = getenv('SITE_GITHUB'),
            header_pages = header_pages
        )

    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    # Auth Routes
    from app.routes.auth import auth
    app.register_blueprint(auth)

    # Home Route
    from app.routes.home.main import h_main
    app.register_blueprint(h_main)

    from app.routes.home.entry import h_entry
    app.register_blueprint(h_entry)

    from app.routes.home.page import h_page
    app.register_blueprint(h_page)

    # Dashboard Routes
    from app.routes.dashboard.main import d_main
    app.register_blueprint(d_main)

    from app.routes.dashboard.entry import d_entry
    app.register_blueprint(d_entry)

    from app.routes.dashboard.page import d_page
    app.register_blueprint(d_page)

    return app
