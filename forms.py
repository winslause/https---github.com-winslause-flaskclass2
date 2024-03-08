from flask_wtf import Form
from wtforms import *


# from wtforms import validators, ValidationError


class ContactForm(Form):
    name = StringField("Name of the student", [validators.InputRequired("Please enter your name")])
    Gender = RadioField("Gender", choices=[('F', 'Female'), ('M', 'Male')])
    Address = TextAreaField("Address")
    email = StringField("Email", [validators.InputRequired("Please enter your email"),
                                  validators.Email("Please enter your email")])
    Age = IntegerField("Age")
    Language = SelectField("Language", choices=[('CPP', 'CPP'), ('Py', 'Python')])
    submit = SubmitField("Send")
