from django.urls import path
from . import views

app_name = 'comments'

urlpatterns = [
	path('create_comment/<int:pk>/', views.CommentCreateView.as_view(), name='create_comment'),
	path('list_comment/', views.CommentListView.as_view(), name='list_comment'),
	path('update_comment/<int:pk>/', views.CommentUpdateView.as_view(), name='update_comment'),
	path('delete_comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='delete_comment')
]