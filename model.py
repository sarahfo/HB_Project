"""Models and database functions for House Hunter project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##############################################################################
# Model definitions

# class User(db.Model):
# 	"""User of House Hunter Website"""

# 	__tablename__ = "users"

# 	email = db.Column(db.String(100), primary_key=True)
# 	password = db.Column(db.String(64), nullable=False)
# 	age = db.Column(db.Integer, nullable=False)

# 	def __repr__(self):
# 		"""Represents the data in a helpful way when printed"""

# 		return "<User email=%s age=%d>" % (self.email, self.age)

# class City(db.Model):
# 	"""Real Estate in City selected by User"""

# 	__tablename__ = "cities"

# 	city_id = db.Column(db.Integer(4), autoincrement=True, primary_key=True)
# 	city = db.Column(db.String(50))


# 	def __repr__(self):
# 		"""Represents the data in a helpful way when printed"""

# 		return "<City=%s>" % (self.city)


class Home(db.Model):
	"""Home in the selected city"""

	__tablename__ = "homes"

	home_id = db.Column(db.Integer(8), autoincrement=True, primary_key=True)
	home_type = db.Column(db.String(50), nullable=True)
	address = db.Column(db.String(80))
	city = db.Column(db.String(50))
	state = db.Column(db.String(2), nullable=True)
	zip_code = db.Column(db.String(5), nullable=True)
	list_price = db.Column(db.Integer, nullable=True)
	beds = db.Column(db.Integer, nullable=True)
	baths = db.Column(db.Integer, nullable=True)
	location = db.Column(db.String(70), nullable=True)
	sqft = db.Column(db.Integer, nullable=True)
	lot_size = db.Column(db.Integer, nullable=True)
	year_built = db.Column(db.Integer, nullable=True)
	parking_spots = db.Column(db.Integer, nullable=True)
	parking_type = db.Column(db.String(20), nullable=True)
	days_on_market = db.Column(db.Integer(3), nullable=True)
	url = db.Column(db.String(120), nullable=True)
	source = db.Column(db.String(60), nullable=True)
	listing_id = db.Column(db.Integer(7), nullable=True)
	original_source =  db.Column(db.String(80), nullable=True)
	favorite = db.Column(db.String(1), nullable=False)
	latitude = db.Column(db.Integer(11), nullable=False)
	longitude = db.Column(db.Integer(11), nullable=False)


	def __repr__(self):
		"""Represents the data in a helpful way when printed"""

		return "<address=%s, home_type=%s, latitude%d>" % (self.city, self.home_type, self.latitude)

# class Home_Type(db.Model):
# 	"""Type of home (condo, SFR, etc.)"""

# 	__tablename__ = "hometype"

# 	home_type_id = db.Column(db.Integer(3), autoincrement=True, primary_key=True)
# 	home_type = db.Column(db.String(50))


# 	def __repr__(self):
# 		"""Represents the data in a helpful way when printed"""

# 		return "<home_type=%s>" % (self.home_type)


