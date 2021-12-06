from flask import Blueprint,render_template,session, url_for, redirect,request
from flask_login import login_required, login_user, logout_user, current_user
from blogproject.user.forms import LoginForm,RegisterForm,AccountForm
from blogproject.models import User
from blogproject import db
from werkzeug.security import check_password_hash

user_blueprint=Blueprint('user',__name__)

@user_blueprint.route('/account',methods=['POST',"GET"])
@login_required
def account():
    form=AccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        return redirect(url_for('user.account'))
    else:
        form.email.data=current_user.email
        form.username.data=current_user.username
        return render_template('account.html',form=form)

    return render_template('account.html')

@user_blueprint.route('/login',methods=['POST','GET'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        u=User.query.filter_by(email=form.email.data).first()
        if check_password_hash(u.password,form.password.data):
            login_user(u)

            next=request.args.get('next')
            return redirect(next or url_for('core.index'))

        
    
    return render_template('login.html',form=form)

@user_blueprint.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('core.index'))

@user_blueprint.route('/register',methods=['GET','POST'])
def register():
    form=RegisterForm()
    if form.validate_on_submit():
        u=User(email=form.email.data,username=form.username.data, password=form.password.data)
        db.session.add(u)
        db.session.commit()
        return redirect(url_for('user.login'))
    return render_template('register.html',form=form)

    