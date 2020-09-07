from app import db

class Page(db.Model):
    id = db.Column(db.Integer, primary_key = True) # Page ID.
    slug = db.Column(db.String(100), nullable = False, unique = True) # Page Slug.
    title = db.Column(db.String(100), nullable = False) # Page Title.
    content = db.Column(db.Text, nullable = False) # Page Content.
    is_active = db.Column(db.Boolean, nullable = False, default = True) # Page Activate.
    created_at = db.Column(
        db.DateTime, nullable = False, default = db.func.now(),
        server_default = db.func.now()
    ) # Psge Create Date.
    updated_at = db.Column(
        db.DateTime, nullable = False, default = db.func.now(),
        server_default = db.func.now(), server_onupdate = db.func.now()
    ) # Page Modify Date.
