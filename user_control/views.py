from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .foms import CustomRegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def index(request):
    return render(request,'index.html',{})


def contact(request):
    return render(request,'contact.html' ,{})

def about(request):
    return render(request,'about.html',{})


@login_required
def resource(request):
    return render(request ,'resourse.html',{})

def register(request):
    if request.method == 'POST':
        register_form = CustomRegisterForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            return redirect ("index")
        else:
            return redirect ("register")
    else:
        register_form = CustomRegisterForm()
        return render (request ,'register.html',{'form':register_form})