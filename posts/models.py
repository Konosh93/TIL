from django.db import models
from django.contrib.auth.models import User
from posts.managers import AuthorManager

# Create your models here.
class Author(User):
	objects = AuthorManager()

	class Meta:
		proxy = True
		ordering = ('username', )


class Post (models.Model):
	title = models.CharField(max_length=255,default="Today I learned ...")
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	text = models.CharField(max_length=255,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	tags = models.CharField(max_length=255)
	likes = models.IntegerField(default=0)

	def __str__(self):
		return self.title

	class Meta:
		ordering = ("-date_created",) 

class Comment(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.CharField(max_length=255,blank=True)
	date_created = models.DateTimeField(auto_now_add=True)
	likes = models.IntegerField(default=0)

	class Meta:
		ordering = ("date_created",) 