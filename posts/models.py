from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post (models.Model):
	title = models.CharField(max_length=255,default="Today I learned ...")
	author = models.ForeignKey(User)
	text = models.CharField(max_length=255,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=255)
	likes = models.IntegerField(default=0)

	class Meta:
		ordering = ("-date_created",) 

class Comment(models.Model):
	author = models.ForeignKey(User)
	post = models.ForeignKey(Post)
	text = models.CharField(max_length=255,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)

	class Meta:
		ordering = ("date_created",) 