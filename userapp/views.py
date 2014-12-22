from django.shortcuts import render, HttpResponseRedirect
from userapp.models import User
from django.views import generic
from django.forms import ModelForm

class UserForm(ModelForm):
	class Meta:
		model = User
		fields = ['first_name', 'last_name', 'email', 'birthday']

class IndexView(generic.ListView):
    template_name = 'userapp/index.html'
    context_object_name = 'user_list'

    def get_queryset(self):
    	return User.objects.all()

def new(request):
	form = UserForm()
	return render(request, 'userapp/new.html', { 'form': form })

def add_new_user(request):
	form = UserForm(request.POST)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('index.html')
	else:
		return render(request, 'userapp/new.html', { 'form': form })
