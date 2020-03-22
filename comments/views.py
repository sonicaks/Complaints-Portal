from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth import get_user_model
User = get_user_model()
from django.http import Http404
from django.urls import reverse_lazy
from student import models as student_models
from . import models

# Create your views here.

class CommentCreateView(LoginRequiredMixin, CreateView):
	fields = ['message']
	model = models.Comment
	template_name = 'comments/create_comment.html'

	def form_valid(self, form):
		self.object = form.save(commit=False)
		complaint = get_object_or_404(student_models.Complaint, pk=self.kwargs['pk'])
		self.object.comment = complaint
		self.object.user = self.request.user
		self.object.save()
		self.success_url = reverse_lazy('student:detail_complaint', kwargs={'pk' : self.kwargs['pk']})

		return super().form_valid(form)

class CommentListView(LoginRequiredMixin, ListView):
	model = models.Comment
	template_name = 'comments/list_comment.html'

	def get_queryset(self):
		try:
			self.user_comments = User.objects.prefetch_related('author').get(username=self.request.user.username)
		except User.DoesNotExist:
			raise Http404

		return self.user_comments.author.all()

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	fields = ['message']
	model = models.Comment
	template_name = 'comments/update_comment.html'
	success_url = reverse_lazy('comments:list_comment')

	def test_func(self):
		return self.get_object().user == self.request.user

	def form_valid(self, form):
		self.object = form.save(commit=False)
		self.object.save()

		return super().form_valid(form)

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = models.Comment
	template_name = 'comments/delete_comment.html'
	success_url = reverse_lazy('comments:list_comment')

	def test_func(self):
		return self.get_object().user == self.request.user