from yelpapi import YelpAPI
import argparse



# yelp_api = YelpAPI(consumer_key, consumer_secret, token, token_secret)
# search_results = yelp_api.search_query(args)
# business_results = yelp_api.business_query(id=business_id, other_args)

# def yelp_search_query(self):
# # make an empty list to hold the stuff you will pass to yelp
# 	# yelp=[]

# 	yelp_search = request.args.getlist('category_filter')

# 	print yelp_search


def get_cat_list():

	yelp_search = requests.args.getlist('category_filter')

	print yelp_search




# def yelp_business_basics(business_entry):
#     """ http://www.yelp.com/developers/documentation/v2/search_api
#         See Businesses structure """
#     return {"name"          : business_entry.get("name"),
#             "image_url"     : business_entry.get("image_url", ""),
#             "rating"        : business_entry.get("rating", "n/a"),
#             "rating_image"  : business_entry.get("rating_img_url"),
#             "address"       : "\n".join(business_entry["location"]["display_address"])}
	