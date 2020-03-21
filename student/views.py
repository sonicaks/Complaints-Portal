from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import Http404
from django.views.generic import CreateView, DeleteView, UpdateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from . import models

# Create your views here.

class CreateComplaintView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
	fields = ['block_number', 'room_number', 'hall', 'roll_number', 'type', 'message']
	model = models.Complaint
	template_name = 'student/create_complaint.html'
	success_url = reverse_lazy('student:status')

	def test_func(self):
		return self.request.user.account_type.all()[0].type == 'STU'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()

		return super().form_valid(form)

class UpdateComplaintView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	fields = ['block_number', 'room_number', 'hall', 'roll_number', 'type', 'message']
	model = models.Complaint
	template_name = 'student/update_complaint.html'
	success_url = reverse_lazy('student:status')

	def test_func(self):
		return self.request.user.account_type.all()[0].type == 'STU' and self.get_object().user == self.request.user

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.user = self.request.user
		self.object.save()

		return super().form_valid(form)

class DeleteComplaintView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = models.Complaint
	template_name = 'student/delete_complaint.html'
	success_url = reverse_lazy('student:status')

	def test_func(self):
		return self.request.user.account_type.all()[0].type == 'STU' and self.get_object().user == self.request.user

class StatusView(LoginRequiredMixin, UserPassesTestMixin, ListView):
	model = models.Complaint
	template_name = 'student/status.html'

	def test_func(self):
		return self.request.user.account_type.all()[0].type == 'STU'

	def get_queryset(self):
		try:
			self.user_complaints = User.objects.prefetch_related('complaints').get(username=self.request.user.username)
		except User.DoesNotExist:
			raise Http404

		return self.user_complaints.complaints.all()