from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .models import Tasks
from django.db import close_old_connections, IntegrityError
from django.urls import reverse
#libreria para pdfs
from django.views.generic import ListView, View

# Create your views here.
def list_Task(request):
    return render(request, "./home/tasks.html", {})

def create_Task(request):
    if request.method != "POST":
        return render(request, "./tasks/create.htm",{})
    else:
        if "cancelar" in request.POST:
            return redirect("./home/tasks.html")

        try:
            print("intentando crear tarea")
            required_fields= []
            pass

        except Exception as e: 
            pass