from django.shortcuts import render, HttpResponseRedirect
from userapp.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.forms import ModelForm

class IndexView(ListView):
    template_name = 'userapp/index.html'
    def get_queryset(self):
    	return User.objects.all()

class UserCreate(CreateView):
	model = User
	fields = ['first_name', 'last_name', 'email', 'birthday']	

class UserUpdate(UpdateView):
    model = User
    fields = ['first_name', 'last_name', 'email', 'birthday']	

class UserDelete(DeleteView):
	model = User
	success_url = '/userapp'
