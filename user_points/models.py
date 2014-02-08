from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from movie.models import Movie, Rate, Comment
import datetime

class Summary(models.Model):
	user = models.ForeignKey(User)
	points = models.IntegerField()
	
class PointMeasure(models.Model):
	COMMENT = 'co'
	VIDEO_COMMENTED = 'vc'
	VIDEO_LIKED = 'vl'
	VIDEO_SHARED = 'vs'
	FB_SHARE = 'fs'
	FB_LIKE = 'fl'
	NEW_VIDEO = 'nv'
	RATE = 'ra'
	RATE_CATEGORIES = 'rc'
	point_categories = (
		(COMMENT, 'Comment'),
		(FB_SHARE, 'Fb_share'),
		(FB_LIKE, 'Fb_like'),
		(NEW_VIDEO, 'New_video'),
		(RATE_CATEGORIES, 'Rate_categories'),
		)
	point = models.IntegerField(default=0)
	category = models.CharField(max_length=2, choices = point_categories)

class UserPoint(models.Model):
	user = models.ForeignKey(User)
	created = models.DateTimeField()
	point = models.ForeignKey(PointMeasure)

@receiver(post_save, sender=Movie)
def save_movie_handler(sender, **kwargs):
	save_points(kwargs['instance'].owner, 'nv')
    
@receiver(post_save, sender=Rate)
def save_rate_handler(sender, **kwargs):
	category = 'ra'
	rate = kwargs['instance']
	if(rate.category != 'rt'):
		category = 'rc'
	save_points(kwargs['instance'].owner, 'rc')
    
@receiver(post_save, sender=Comment)
def save_comment_handler(sender, **kwargs):
    save_points(kwargs['instance'].owner, 'co')
    
def save_points(user, point_cagetory):
	 UserPoint.objects.create(user=user, 
    				created = datetime.datetime.now(), 
    				point= PointMeasure.objects.get(category=point_cagetory))
