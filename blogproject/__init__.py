from flask import Flask,render_template
from flask.helpers import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import os


db_path=os.path.join(os.path.abspath(os.path.dirname(__file__)),'starkDB.db')

app=Flask(__name__)

app.config['SECRET_KEY']='helloworld'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///'+db_path


db=SQLAlchemy(app)
Migrate(app,db)

login_manager=LoginManager()
login_manager.init_app(app)
login_manager.login_view='user.login'
from blogproject.core.views import core_blueprint
from blogproject.user.views import user_blueprint
from blogproject.blog.views import blog_blueprint


app.register_blueprint(core_blueprint)
app.register_blueprint(user_blueprint)
app.register_blueprint(blog_blueprint)


