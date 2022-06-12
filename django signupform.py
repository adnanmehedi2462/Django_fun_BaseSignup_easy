from django.contrib import messages
from urllib import request
from django.http import HttpResponse

from django.views.generic import View
from django.contrib.auth.forms import UserCreationForm
from .forms import createform
from django.contrib.auth.models import User
from django.shortcuts import render,get_object_or_404,HttpResponse,Http404,redirect,HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy

# Create your views here.
# def  register(request):
#     url = request.META.get('HTTP_REFERER')
#     if request.method == "POST":  
#         username=request.POST['username']
#         password=request.POST['password']
#         confirm_password=request.POST['confirm_password']

#         if password == confirm_password:
#             if User.objects.filter(username=username).exists():
#                 messages.error(request, 'User name already exists !!')
#             else:
#                 user=User.objects.create_user(username=username,password=password)
#                 user.is_active=True
#                 user.is_staff=True
#                 user.save()
#                 return redirect ("/")

#         else:
#             messages.error(request, 'Password not match !!')
#             return HttpResponseRedirect(url)
         
            
            

#     return render(request,"register.html")
    


# forms.py

from dataclasses import fields
from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class createform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password1','password2']



# end forms.py













    

def register(request):
    url = request.META.get('HTTP_REFERER')
    
    form=createform()
    
    if request.method=='POST': 
        
        form=UserCreationForm(request.POST)      
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get("username")
            
            messages.success(request, 'Account create successfully by ' + username, extra_tags='alert')
            return redirect("/")
                                  
        else:
            messages.success(request,'something Wrong !!')

            
    context={
        "form":form
    }
    return render(request,"register.html",context)
    
    
