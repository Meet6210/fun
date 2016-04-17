from flask.ext.wtf import Form
from wtforms import DecimalField

class LoginForm(Form):
    
    Stock = DecimalField('Stock')
    Pe = DecimalField('Pe')
    t = DecimalField('t')
    
"""
Web forms are represented in Flask-WTF as classes, subclassed from base class
Form. A form subclass simply defines the fields of the form as class variables.

We imported the Form class, and the form field class that we need ie. the 
DecimalField.
  
"""
