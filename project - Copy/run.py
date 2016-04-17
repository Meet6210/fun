#!flask/bin/python
from app import app
app.run(debug=True)

"""
The script simply imports the app variable from our app package and invokes
 its run method to start the server. The app variable holds 
 the Flask instance.
 
 Running the app in debug mode (app.debug = True or app.run(debug=True) will 
 show an interactive traceback and console in the browser when there is an error.

To start the app,this script is run.
"""