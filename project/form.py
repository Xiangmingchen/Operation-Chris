from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, BooleanField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = IntegerField('Password', validators=[DataRequired()])

class OrderForm(FlaskForm):
    item = StringField('item')
    patty = SelectField('Patty', choices=[('1','1'),('2','2'),('3','3')])
    nobun = BooleanField('nobun')
    cheese = BooleanField('cheese')
    bacon = BooleanField('bacon')