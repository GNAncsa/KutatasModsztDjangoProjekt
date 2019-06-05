# t2048/views.py
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
import json
import os

def show_2048(request):
    return render(request, 'index.html')


class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
	
def testcall(request):
    data = {}
    data['scores'] = []
    if os.stat('data.txt').st_size!=0:
        with open('data.txt') as json_file:
            old_data = json.load(json_file)
        szerepel = False
        for p in old_data['scores']:
            int_old_score = int(p['score'])
            int_new_score = int(request.POST['score'])
            if request.POST['user'] != p['user']:
                data['scores'].append({
                    'user': p['user'],
                    'score': p['score'],
                })
            else:
                szerepel = True
                if int_old_score < int_new_score:
                    data['scores'].append({
                        'user': request.POST['user'],
                        'score': request.POST['score'],
                    })
                else:
                    data['scores'].append({
                        'user': p['user'],
                        'score': p['score'],
                    })				
        if not szerepel:
            data['scores'].append({
                'user': request.POST['user'],
                'score': request.POST['score'],
            })        
    else:
        data['scores'].append({
            'user': request.POST['user'],
            'score': request.POST['score'],
        })         
    with open('data.txt', 'w') as outfile:
        json.dump(data, outfile)
    return HttpResponse(request.POST['user'])