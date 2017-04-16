from app import db
from app import app

import sys

class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	latitude = db.Column(db.Float(20))
	longitude = db.Column(db.Float(20))
	
	def __init__(self, latitude, longitude):
		self.latitude = latitude
		self.longitude = longitude

	def __repr__(self):
		return '%s, %s ' % (self.latitude, self.longitude)


	def serialize(self):
		return {
			'latitude': self.latitude,
			'longitude': self.longitude
		}
