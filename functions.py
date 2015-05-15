from yelpapi import YelpAPI
import argparse



yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)
search_results = yelp_api.search_query(args)
business_results = yelp_api.business_query(id=business_id, other_args)

def yelp_search_query(self):
# make an empty list to hold the stuff you will pass to yelp
	yelp=[]
	yelp_search = self.request.get('category_filter')

	if yelp_search:
		# get the stuff passed from the form - if the box is checked, pass the value into yelp API.
