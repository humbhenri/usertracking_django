from django.shortcuts import render, HttpResponseRedirect
from userapp.models import User
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'userapp/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
    	return User.objects.all()

def new(request):
	return render(request, 'userapp/new.html', {})

def add_new_user(request):
	user = User()
	return HttpResponseRedirect('index.html')
