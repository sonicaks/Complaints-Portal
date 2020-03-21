from django.contrib.auth import get_user_model
User = get_user_model()
from django.views.generic import ListView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import Http404
from django.urls import reverse_lazy
from student import models

# Create your views here.

class UpdateStatusView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	fields = ['status']
	model = models.Complaint
	template_name = 'worker/update_status.html'
	success_url = reverse_lazy('worker:all_complaints')

	def test_func(self):
		return self.request.user.account_type.all()[0].type == self.get_object().type

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()

		return super().form_valid(form)

class ComplaintListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = models.Complaint
	template_name = 'worker/complaint_list.html'

	def test_func(self):
		return self.request.user.account_type.all()[0].type != 'STU'

	def get_queryset(self):
		try:
			self.all_complaints = models.Complaint.objects.filter(type=self.request.user.account_type.all()[0].type)
		except:
			raise Http404

		return self.all_complaints