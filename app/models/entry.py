from app import db

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key = True) # Entry ID.
    slug = db.Column(db.String(100), nullable = False, unique = True) # Entry Slug.
    title = db.Column(db.String(100), nullable = False) # Entry Title.
    content = db.Column(db.Text, nullable = False) # Entry Content.
    is_active = db.Column(db.Boolean, nullable = False, default = True) # Entry Activate.
    created_at = db.Column(
        db.DateTime, nullable = False, default = db.func.now(),
        server_default = db.func.now()
    ) # Entry Create Date.
    updated_at = db.Column(
        db.DateTime, nullable = False, default = db.func.now(),
        server_default = db.func.now(), server_onupdate = db.func.now()
    ) # Entry Modify Date.
