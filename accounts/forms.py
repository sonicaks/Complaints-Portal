from django import forms
from django.contrib.auth import get_user_model
User = get_user_model()
from registration.forms import RegistrationFormUniqueEmail
from django.core.exceptions import ValidationError
from . import models

class UserCreateForm(RegistrationFormUniqueEmail):
	categories = (
		('STU', 'Student'),
		('ELE', 'Electrician'),
		('PLU', 'Plumber'),
		('GLA', 'Glazier'),
		('CAR', 'Carpenter')
	)

	type = forms.CharField(max_length=3, widget=forms.Select(choices=categories))

	class Meta:
		fields = ('first_name', 'last_name', 'username', 'email', 'type', 'password1', 'password2')
		model = User

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)