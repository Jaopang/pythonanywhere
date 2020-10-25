from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .models import Destination
from .models import *
from .forms import Destinationform



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


def aboutcow(req):
    return render(req, 'myweb/aboutcow.html')

def index(req):
    Destinations = Destination.objects.all()
    return render(req, 'myweb/index.html', {'Destinations': Destinations})

def post(request):
    if request.method == 'POST':
        form = Destinationform(request.POST)

        if form.is_valid():
            a = form.save()
            a.save()
            return redirect("/index")
    else:
        form = Destinationform()
        context = {'form': form}
        return render(request, 'myweb/post.html', context)
