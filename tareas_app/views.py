from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
#from .models import Users
from django.db import close_old_connections, IntegrityError
from django.urls import reverse

# Create your views here.
def list_Task(request):
    return render(request, "./home/tasks.html", {})

def create_Task(request):
    return render(request,"./tasks/create.html",{})