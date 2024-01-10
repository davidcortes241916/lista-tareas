from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import ValidationError
from .models import Users
from django.db import close_old_connections, IntegrityError
from django.urls import reverse


# Create your views here.
def home(request):
    return render(request, "./home/home.html", {})

def loginSignOn(request):
    if request.method != "POST":
       return render(request, "./login/login.html", {})
    else:
        if "cancelar" in request.POST:
            return redirect("signIn")

        try:
            #quitar los prints cuando esto funcione bien
            print("intentando crear usuario")
            required_fields = ["name", "last_name", "date_birthday", "rol", "email", "password1"]

            for field in required_fields:  
                if not request.POST.get(field):
                    print("todos los campos son necesarios")
                    messages.error(request, "Debe completar todos los campos!")
                    return redirect("signOn")

            email= request.POST["email"]
            if Users.objects.filter(email=email).exists():
                print("correo ya existe")
                messages.error(request, f"El correo electronico {email} ya existe!")
                return redirect("signOn")

            user= Users.objects.create_user(
                first_name= request.POST["name"],
                last_name= request.POST["last_name"],
                date_birthday= request.POST["date_birthday"],
                rol_user= request.POST["rol"],
                email= email,
                password= request.POST["password1"],
            )
            user.is_active= True
            user.save()
            print("usuario creado")
            return redirect("signIn")
            #tambien le falta una url al que enviarse  
        
        except Exception as e:
            print(f"error al crear usuario: {e}")
            close_old_connections()
            error_message= f"Error al registrar usuario: {e}"
            return render(request, "./login/login.html", {'error_message': error_message})    

def loginSignIn(request):

    if request.method != "POST":
        return render(request, "./login/signIn.html", {})
    else:
        email = request.POST["email"]
        password = request.POST["password1"]
        
        try:
            user = authenticate(request, email=email, password=password)
            print(user)
            if user is not None and user.is_active:
                login(request, user)
                return redirect("home/")
            else:
                print("Usuario no activo")
                messages.error(request, "Correo o contraseña incorrectos!")
                return render(request, "./login/signIn.html", {})
        except ValidationError as e:
            print("Error de validación:", e)
            messages.error(request, "Correo o contraseña incorrectos!")
            return render(request, "./login/signIn.html", {})
    