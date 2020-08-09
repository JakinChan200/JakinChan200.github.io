from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
        
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    pw_hash = db.Column(db.String(128))
    
    def set_pw(self, password):
        self.pw_hash = generate_password_hash(password)
        
    def check_pw(self, password):
        return check_password_hash(self.pw_hash, password)

class ExtendedUser(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    bday = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    totalposts = db.Column(db.Integer, nullable=False)
    
class Post(db.Model):
    
    max_post_len = 200
    
    postid = db.Column(db.Integer, primary_key=True)
    contents = db.Column(db.String(max_post_len))
    time_posted = db.Column(db.DateTime, index=True, default=datetime.utcnow)