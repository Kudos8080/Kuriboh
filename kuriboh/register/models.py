import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class User(models.Model):
	username = models.CharField(max_length=16)
	password = models.CharField(max_length=16)
	register_date = models.DateTimeField('register date')

	def __str__(self):
		return self.username



