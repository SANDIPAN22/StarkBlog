from blogproject import app,db
from flask import render_template, Blueprint
from blogproject.models import Blog,User

core_blueprint= Blueprint('core',__name__)
@core_blueprint.route('/')
def index():
    blogs=Blog.query.order_by(Blog.date.desc())
    
    return render_template('index.html',blogs=blogs)