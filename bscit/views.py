from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import auth


from django.contrib import messages

from . models import question
from . forms import question_form
from . models import Events
from .models import notice
from .models import profile

from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

def index(request):
  model = Events.objects.all()
  model1 = notice.objects.all()

  if request.method =='POST':
    form = question_form(request.POST)
    if form.is_valid():
      form.save()
      return redirect('index')
  else:
    form = question_form()  
  return render(request,'index.html',{'form':form,'model':model,'model1':model1})


def syllabus(request):
  return render(request,'syllabus.html')

def carrier(request):
  return render(request,'carrier.html')  

def about_us(request):
  return render(request,'about.html')  

def login(request):
  if request.method == 'POST':
    username = request.POST['user']
    password = request.POST['pas']
    try:
      user = auth.authenticate(username=username,password=password)
      if user is not None:
        
        auth.login(request,user)
    
        return render(request,'profile_view.html')
      else:
        messages.warning(request, 'Username and password did not match')
    except ObjectDoesNotExist:
      print("Invalid user")
  return render(request,'login2.html')


  
def logout(request):
    auth.logout(request)
    return redirect('index')

def team(request):
  return render(request,'team.html')


def teacher_profile(request):
  return render(request,'teacher.html')