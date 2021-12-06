from sqlalchemy.orm import backref
from blogproject import db,login_manager
from werkzeug.security import generate_password_hash
from datetime import datetime
from flask_login import UserMixin,current_user

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(db.Model,UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(100), unique=True, nullable=False)
    email=db.Column(db.String(100),unique=True, nullable=False)
    password=db.Column(db.String(128))

    posts=db.relationship('Blog',backref='User',lazy=True)


    def __init__(self,username,email,password):
        
        self.username=username
        self.email=email
        self.password=generate_password_hash(password)
    def __repr__(self):
        return f"Name: {self.name}    email:  {self.email}"


class Blog(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(50),nullable=False)
    text=db.Column(db.String(150),nullable=False)
    date=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False, )

    def __init__(self,title,text,user_id):
        self.title=title
        self.text=text
        self.user_id=user_id
    

