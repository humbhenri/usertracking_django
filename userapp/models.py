from django.db import models

class User(models.Model):
	"""docstring for User"""
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	birthday = models.DateTimeField()