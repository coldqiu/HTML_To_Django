from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm
from models import User

# Create your views here.


def index(request):
	return render_to_response('index.html',{})

def signup(request):
	if request.method=="POST":
		uf = UserForm(request.POST)
 		print uf
		if uf.is_valid():
			username = uf.cleaned_data['username'] 
			password = uf.cleaned_data['password'] 
			print username,password
			User.objects.create(username=username, password=password)
			return HttpResponseRedirect('/login/')
		else:
			return HttpResponse('is_valid() failed')
	else:
		uf = UserForm()
		return render_to_response('signup.html', {'uf': uf})

	return render_to_response('signup.html',{})

def login(request):
	us = UserForm()
	if request.method=="POST":
		us = UserForm(request.POST)
		print us
		if us.is_valid():
			username = us.cleaned_data['username']
			password = us.cleaned_data['password']
			print username,password
			Users=User.objects.filter(username__exact=username, password__exact=password)
			if Users:
				request.session['username']=username
				return HttpResponseRedirect('/index/')
			else:
				return HttpResponseRedirect('/login/')
	else:
		return render_to_response('login.html', {'us': us})

			
def indexed(request):
	username = request.session.get('username','somebody')
	return render_to_response('indexed.html', {'username':username})
	#return HttpResponse('ok , login')

def logout(request):
	del request.session['username']
	return render_to_response('logout.html',{})
