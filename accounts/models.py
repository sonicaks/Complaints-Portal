from django.db import models
from django.contrib import auth
from django.contrib.auth import get_user_model
LoggedInUser = get_user_model()

# Create your models here.

class User(auth.models.User, auth.models.PermissionsMixin):
	def __str__(self):
		return '@{}'.format(self.username)

class Type(models.Model):
	user = models.ForeignKey(LoggedInUser, on_delete=models.CASCADE, related_name='account_type')

	categories = (
		('STU', 'Student'),
		('ELE', 'Electrician'),
		('PLU', 'Plumber'),
		('GLA', 'Glazier'),
		('CAR', 'Carpenter')
	)

	type = models.CharField(max_length=3, choices=categories)

	def __str__(self):
		return self.user.username