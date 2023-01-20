from flask_wtf import Form
from wtforms import StringField, IntegerField, TextAreaField, SubmitField, RadioField, \
   SelectField

from wtforms import validators

class ContactForm(Form):
   name = StringField("Name Of Student", [validators.DataRequired("Please enter your name.")])
   gender = RadioField('Gender', choices = [('M','Male'),('F','Female')])
   address = TextAreaField("Address")
   
   email = StringField("Email",[validators.DataRequired("Please enter your email address."),
      validators.Email("Please enter your email address.")])
   
   age = IntegerField("Age")
   language = SelectField('Languages', choices = [('cpp', 'C++'), 
      ('py', 'Python')])
   submit = SubmitField("Send")