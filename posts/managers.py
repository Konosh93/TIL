from django.db import models

class AuthorManager(models.Manager):
	def get_by_natural_key(self, username):
		return self.get(username=username)