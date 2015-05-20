"""House Hunter Project"""

import os
#from functions import get_cat_list
import argparse
import rauth
import time
import json, requests, pprint
from yelpapi import YelpAPI
from datetime import date
from flask import Flask, render_template, redirect, request, flash, session
from flask_debugtoolbar import DebugToolbarExtension

# from model import User, connect_to_db, db

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

"""Gets the list of user-selected categories and location and sends them to Yelp API"""

# This syntax returns the user-checked items as a list
        yelp_search_selection = request.args.getlist('category_filter')

# now join them for proper formatting.
        yelp_search = ",".join(yelp_search_selection)
 
        # data = get_results(make_search_params(yelp_search, yelp_location))

# This grabs the location selected from the drop-down.
        yelp_location = request.args['location']

# Call the functions and make it work!
        get_results(make_search_parameters(yelp_search, yelp_location))

# I'm just doing the render template to be superstitious.
    return render_template("base.html")


def make_search_parameters(yelp_search, yelp_location):
    """Yelp API defines the key names for the parameters."""

    params = {}
    params['category_filter'] = yelp_search
    params ["location"] = yelp_location
    ## params ['limit'] = TBD
   
    return params

def get_results(params):
    """OAuth Session with secret keys, sourced from OS."""

    auth_session = rauth.OAuth1Session(
        consumer_key = os.environ['YELP_CONSUMER_KEY'],
        consumer_secret = os.environ['YELP_CONSUMER_SECRET'],
        access_token = os.environ['YELP_ACCESS_TOKEN_KEY'],
        access_token_secret = os.environ['YELP_ACCESS_TOKEN_SECRET'])

    request = auth_session.get("http://api.yelp.com/v2/search", params=params)   
    # URL example for San Francisco: api.yelp.com/v2/search/?location=San Francisco, CA&limit=13&category_filter=yoga

    #Transforms the JSON API response into a Python dictionary
    data = json.loads(request.text)
    #data = request.json()
    auth_session.close()
    pprint.pprint(data)
    # return data


if __name__ == '__main__':
    app.run(debug=True)