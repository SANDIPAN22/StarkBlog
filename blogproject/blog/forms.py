from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import InputRequired

class Createpost(FlaskForm):
    title=StringField("Title:", validators=[InputRequired()])
    text=StringField("Text:",validators=[InputRequired()])
    submit=SubmitField("Publist !")

class Updatepost(FlaskForm):
    title=StringField("Title:", validators=[InputRequired()])
    text=StringField("Text:",validators=[InputRequired()])
    submit=SubmitField("Update !") 
