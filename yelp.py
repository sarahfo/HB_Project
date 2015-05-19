
import os
import rauth
import time
import json


def main():
	locations = [(37.78,-122.41)]
	api_calls = []
	for lat,long in locations:
		params = get_search_parameters(lat,long)
		api_calls.append(get_results(params))
		# Be a good internet citizen and rate-limit yourself
		time.sleep(1.0)

	print api_calls

def get_results(params):
 
	#Obtain these from Yelp's manage access page
	#Good practice of getting the key from somewhere else other than storing it in your db
	consumer_key=os.environ['YELP_CONSUMER_KEY']
	consumer_secret=os.environ['YELP_CONSUMER_SECRET']
	token=os.environ['YELP_ACCESS_TOKEN_KEY']
	token_secret=os.environ['YELP_ACCESS_TOKEN_SECRET']
	
	session = rauth.OAuth1Session(
		consumer_key = consumer_key
		,consumer_secret = consumer_secret
		,access_token = token
		,access_token_secret = token_secret)
		
	request = session.get("http://api.yelp.com/v2/search",params=params)
	
	#Transforms the JSON API response into a Python dictionary
	data = request.json()
	session.close()
	
	return data	

# We are going to make a call to Yelp API.  First, define the search parameters.  I'm going to set this
# at grocery for now, but adjust later.  This request is asking for you to pass it a lat & longitude, I'll use
# SF for now and manually enter it: 37.783, -122.41
def get_search_parameters(lat,long):
  #See the Yelp API for more details - it wants a lat, longitude
	params = {}
	params["category_filter"] = "grocery"   # this will eventually come from the form.
	params["ll"] = "{},{}".format(str(lat),str(long))  # this will eventually come from the map.
	params["radius_filter"] = "2000"
	params["limit"] = "10"
 
  	return params
 
if __name__=="__main__":
	main()