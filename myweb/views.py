from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm


def index(req):
	return render(req, 'myweb/index.html' )

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            raw_password = form.cleaned_data['password1']
            user = authenticate(request,username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'myweb/register.html', {'form': form})

def post(req):
    return render(req, 'myweb/post.html')

def aboutcow(req):
    return render(req, 'myweb/aboutcow.html')
    