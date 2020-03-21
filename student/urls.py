from django.urls import path
from . import views

app_name = 'student'

urlpatterns = [
	path('create_complaint/', views.CreateComplaintView.as_view(), name='create_complaint'),
	path('update_complaint/<int:pk>/', views.UpdateComplaintView.as_view(), name='update_complaint'),
	path('delete_complaint/<int:pk>/delete/', views.DeleteComplaintView.as_view(), name='delete_complaint'),
	path('status/', views.StatusView.as_view(), name='status')
]