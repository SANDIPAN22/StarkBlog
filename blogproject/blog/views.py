from flask import Blueprint,redirect, url_for,request
from flask.templating import render_template
from flask_login import current_user, login_user, logout_user
from flask_login.utils import login_required
from blogproject.models import Blog
from blogproject import db
from blogproject.blog.forms import Createpost,Updatepost

blog_blueprint=Blueprint('blog',__name__)

@blog_blueprint.route('/createpost',methods=['POST','GET'])
@login_required
def createpost():
    form=Createpost()
    if form.validate_on_submit():
        b=Blog(title=form.title.data,text=form.text.data,user_id=current_user.id)
        db.session.add(b)
        db.session.commit()
        return redirect(url_for('core.index'))

    return render_template('createpost.html',form=form)

@blog_blueprint.route('/deletepost',methods=['GET'])
def deletepost():
    b=Blog.query.filter_by(id=request.args.get('blog_post_id')).first()
    db.session.delete(b)
    db.session.commit()
    return redirect(url_for('core.index'))
    

@blog_blueprint.route('/updatepost',methods=['GET','POST'])
@login_required
def updatepost():
    form=Updatepost()
    b=Blog.query.filter_by(id=request.args.get('blog_post_id')).first()

    if form.validate_on_submit():
        b.text=form.text.data
        b.title=form.title.data
        db.session.commit()
        return redirect(url_for('core.index'))
    form.text.data=b.text
    form.title.data=b.title
    return render_template('createpost.html',form=form)
        

    

@blog_blueprint.route('/displaypost',methods=['GET'])
def displaypost():
    b_id=request.args.get('blog_post_id')
    b=Blog.query.filter_by(id=b_id).first()
    return render_template('displaypost.html',blog=b)