from django.db import models
from django.contrib.auth.models import User
from djangoratings.fields import RatingField


class Movie(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	creation_date = models.DateTimeField('creation date')
	trailer_link = models.CharField(max_length=200)
	slug = models.CharField(max_length = 200)
	year = models.DateTimeField()
	owner = models.ForeignKey(User)	
	def __str__(self):
		return self.title

class Rate(models.Model):
	RATE = 'rt'
	ACTION = 'ac'
	CALM = 'ca'
	HAPPY = 'ha'
	SAD = 'sa'
	CULT = 'cu'
	TRASH = 'tr'
	UNKNWON = 'un'
	FAMOUS = 'fa'
	movie_gender = (
		(RATE, 'Rate'),
		(ACTION, 'Action'),
		(CALM, 'Calm'),
		(HAPPY, 'Happy'),
		(SAD, 'Sad'),
		(CULT, 'Cult'),
		(TRASH, 'Trash'),
		(UNKNWON, 'Unknown'),
		(FAMOUS, 'Famous'),
		)
	owner = models.ForeignKey(User)
	rate = models.IntegerField(null = False, default= 0)
	category = models.CharField(max_length=2, choices = movie_gender, default=RATE)
	film = models.ForeignKey(Movie)
	def __str__(self):
		return str(self.film)+': '+str(self.rate) +' - '+str(self.category)

class Comment(models.Model):
	owner = models.ForeignKey(User)
	comment = models.CharField(max_length=200)
	film = models.ForeignKey(Movie)
	rating = RatingField(range=2, can_change_vote=True, allow_delete=True)
	created_at = models.DateTimeField()
	def __str__(self):
		return str(self.film)+': '+str(self.owner) +' - '+str(self.comment)



