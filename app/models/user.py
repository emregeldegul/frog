from app import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True) # User ID.
    email = db.Column(db.String(70), nullable = False, unique = True) # User E-Mail.
    password = db.Column(db.String(32), nullable = False) # User Password.
    name = db.Column(db.String(30), nullable = False) # User Name.
    note = db.Column(db.Text, nullable = True) # User Note.
    created_at = db.Column(db.DateTime, default = db.func.now(), nullable = False) # User Create Date.

    def generate_password_hash(self, password):
        """
            This function is for securely generating password digits.
        """
        self.password = generate_password_hash(password)

    def check_password(self, password):
        """
            This function has been added for login verification.
        """
        return check_password_hash(self.password, password)
