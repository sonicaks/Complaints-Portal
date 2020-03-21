from django.views.generic import ListView
from django.http import Http404
from student import models

class HomePage(ListView):
	model = models.Complaint
	template_name = 'index.html'

	def get_queryset(self):
		try:
			self.all_complaints = models.Complaint.objects.all()
		except:
			raise Http404

		return self.all_complaints