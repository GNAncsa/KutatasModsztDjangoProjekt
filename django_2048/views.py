# accounts/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
	
def home(request):
	return render(request, 'home.html')

def testcall(request):
    return HttpResponse(request.POST['text'])