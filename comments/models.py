from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from student import models as complaint_model
import misaka

# Create your models here.

class Comment(models.Model):
	comment = models.ForeignKey(complaint_model.Complaint, on_delete=models.CASCADE, related_name='comments')
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author')
	created_at = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	message_html = models.TextField(editable=False)

	def save(self, *args, **kwargs):
		self.message_html = misaka.html(self.message)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.message

	class Meta:
		ordering = ['-created_at']