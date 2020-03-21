from django.urls import reverse_lazy
from registration.backends.default.views import RegistrationView
from . import forms
from . import models as account_models

# Create your views here.

class RegisterView(RegistrationView):
	form_class = forms.UserCreateForm
	template_name = 'registration/registration_form.html'

	def register(self, form):
		self.object = form.save(commit=True)
		self.object.save()

		account_models.Type.objects.create(user=self.object, type=form.cleaned_data.get('type'))

		return super(RegisterView, self).register(form)