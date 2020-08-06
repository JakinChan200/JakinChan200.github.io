from .app import db
from datetime import datetime

'''class Task(db.Model):
    __tablename__= 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode, nullable=False)
    pw = db.Column(db.Unicode)
    date_made = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship("user", back_populates="tasks")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.creation_date = datetime.now()'''
        
class User(db.Model):

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.Unicode, nullable=False)
    email = db.Column(db.Unicode, nullable=False)
    password = db.Column(db.Unicode, nullable=False)
    token = db.Column(db.Unicode, nullable=False)

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)
        self.token = secrets.token_urlsafe(64)