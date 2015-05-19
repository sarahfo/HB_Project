"""House Hunter Project"""

import os
#from functions import get_cat_list

from yelpapi import YelpAPI
import argparse
import rauth
import time

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
    print request.method
    if request.args:
    # return render_template("base.html")


    # """Gets the list of user-selected categories and sends them to Yelp API"""
# The above syntax should return the checked items as a list
        yelp_search_selection = request.args.getlist('category_filter')

# now make them non-unicode   
        yelp_search = ",".join(yelp_search_selection)
 
# Print Yelp Search list to confirm they aren't unicode and they look nice.
    # data = get_results(make_search_params(yelp_search))
        get_results(make_search_parameters(yelp_search))

#I'm just doing the render template to be superstitious.
    return render_template("base.html")


def make_search_parameters(yelp_search):
    #Yelp API defines the key names to pass in as parameters.
    params = {}
    params['category_filter'] = yelp_search
    params ["location"] = "Chicago, IL"
    ## params ['limit'] = TBD
    # print params
    return params

def get_results(params):
    #OAuth Session with secret keys, sourced from OS.

    auth_session = rauth.OAuth1Session(
        consumer_key = os.environ['YELP_CONSUMER_KEY'],
        consumer_secret = os.environ['YELP_CONSUMER_SECRET'],
        access_token = os.environ['YELP_ACCESS_TOKEN_KEY'],
        access_token_secret = os.environ['YELP_ACCESS_TOKEN_SECRET'])

    request = auth_session.get("http://api.yelp.com/v2/search", params=params)
    
    #Transforms the JSON API response into a Python dictionary
    data = request.json()
    auth_session.close()
    
    # return data
    print data


# URL example for San Francisco: api.yelp.com/v2/search/?location=San Francisco, CA&limit=13&category_filter=yoga

if __name__ == '__main__':
    app.run(debug=True)