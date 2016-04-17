from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from app import views

"""
The script above simply creates the application object (of class Flask) and 
then imports the views module. 
Do not confuse app the variable (which gets assigned the Flask instance) with
 app the package (from which we import the views module).


The views are the handlers that respond to requests from web browsers or 
other clients. In Flask handlers are written as Python functions. Each view
 function is mapped to one or more request URLs.
 
Flask has to be told to read and use config file.
"""