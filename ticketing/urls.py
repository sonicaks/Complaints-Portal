"""ticketing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls)
]

# Index page
urlpatterns += [
    path('', views.HomePage.as_view(), name = 'home')
]

# Django site authentication urls
urlpatterns += [
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('registration.backends.default.urls'))
]

# Student urls
urlpatterns += [
    path('student/', include('student.urls'))
]

# Worker urls
urlpatterns += [
    path('worker/', include('worker.urls'))
]

# Comment urls
urlpatterns += [
    path('comments/', include('comments.urls'))
]