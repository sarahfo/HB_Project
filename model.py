"""Models and database functions for House Hunter project."""

from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


##############################################################################
# Model definitions

class User(db.Model):
	"""User of House Hunter Website"""

	__tablename__ = "users"

	email = db.Column(db.String(100), primary_key=True)
	password = db.Column(db.String(64), nullable=False)
	age = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		"""Represents the data in a helpful way when printed"""

		return "<User email=%s age=%d>" % (self.email, self.age)
