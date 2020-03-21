from django.urls import path
from . import views

app_name = 'worker'

urlpatterns = [
	path('update_status/<int:pk>/', views.UpdateStatusView.as_view(), name='update_status'),
	path('all_complaints/', views.ComplaintListView.as_view(), name='all_complaints')
]