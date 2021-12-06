from flask_wtf import FlaskForm
from blogproject.models import User
from wtforms import SubmitField, StringField, PasswordField, EmailField
from wtforms.validators import InputRequired
from wtforms import ValidationError

class RegisterForm(FlaskForm):
    username=StringField("Username",validators=[InputRequired()])
    email=EmailField("Email",validators=[InputRequired()])
    password=PasswordField("Password",validators=[InputRequired()])
    submit=SubmitField("Register")

    def check_username(self,field):
        print("SSSSSSSS=> "+field)
        if User.query.filter_by(username=field.data).first():
            raise ValidationError
    def check_email(self,field):
        print("CCCCC=> "+field)
        if User.query.filter_by(email=field.data).first():
            raise ValidationError



class LoginForm(FlaskForm):
    email=EmailField("Email",validators=[InputRequired()])
    password=PasswordField("Password",validators=[InputRequired()])
    submit=SubmitField("Login")

class AccountForm(FlaskForm):
    username=StringField("Username")
    email=EmailField("Email")
    submit=SubmitField("Update")

    def check_username(self,field):
        print("SSSSSSSS=> "+field)
        if User.query.filter_by(username=field.data).first():
            raise ValidationError
    def check_email(self,field):
        print("CCCCC=> "+field)
        if User.query.filter_by(email=field.data).first():
            raise ValidationError



    

