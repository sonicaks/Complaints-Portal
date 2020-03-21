from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
import misaka

# Create your models here.

class Complaint(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='complaints')
	created_at = models.DateTimeField(auto_now_add=True)
	message = models.TextField()
	message_html = models.TextField(editable=False)

	categories = (
		('ELE', 'Electrical'),
		('PLU', 'Plumbing'),
		('GLA', 'Glass'),
		('CAR', 'Wood')
	)

	halls = (
		('MV', 'MV Hall'),
		('GDB', 'GDB Hall'),
		('DBA', 'DBA Hall'),
		('MSS', 'MSS Hall'),
		('VS', 'VS Hall'),
		('SD', 'SD Hall'),
		('HB', 'HB Hall'),
		('SSB', 'SSB Hall'),
		('KMS', 'KMS Hall'),
		('CVR', 'CVR Hall')
	)

	statuses = (
		('PEN', 'Pending'),
		('PRO', 'In progress'),
		('COM', 'Finished')
	)

	block = (
		('A', 'A'),
		('B', 'B'),
		('C', 'C'),
		('D', 'D')
	)

	type = models.CharField(max_length=3, choices=categories)
	hall = models.CharField(max_length=3, choices=halls)
	status = models.CharField(max_length=3, choices=statuses, default='PEN')
	block_number = models.CharField(max_length=1, choices=block)
	room_number = models.CharField(max_length=3)
	roll_number = models.CharField(max_length=9)

	def save(self, *args, **kwargs):
		self.message_html = misaka.html(self.message)
		super().save(*args, **kwargs)

	def __str__(self):
		return self.message

	class Meta:
		ordering = ['-created_at']