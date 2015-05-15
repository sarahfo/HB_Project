"""House Hunter Project"""

import os

from datetime import date
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

#from model import User, connect_to_db, db

app = Flask(__name__)

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"


# Normally, if you use an undefined variable in Jinja2, it fails silently.
# This is horrible. Fix this so that, instead, it raises an error.
#app.jinja_env.undefined = StrictUndefined


@app.route('/')
def index():
    """Homepage."""
    print "this runs"
    return render_template("base.html")




if __name__ == '__main__':
	app.run(debug=True)