from django.urls import path
from django.views.generic.base import TemplateView

from . import views


urlpatterns = [
    path('', views.home, name='home'),
	path('signup/', views.SignUp.as_view(), name='signup'),
	path('my-ajax-test/', views.testcall, name='testcall'),
]