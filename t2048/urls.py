# t2048/urls.py
from django.urls import path

from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
	path('my-ajax-test/', views.testcall),
]