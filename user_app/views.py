from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Users

# Create your views here.
def formView(request):
    return render(request, "./login/signIn.html", {})

def loginSignOn(request):
    if request.method != "POST":
       return render(request, "./login/login.html", {})
    else:
        try:
            #quitar los prints cuando esto funcione bien
            print("intentando crear usuario")
            required_fields = ["name", "last_name", "date_birthday", "rol", "email", "password1"]

            for field in required_fields:  
                if not request.POST.get(field):
                    messages.error(request, "Debe completar todos los campos!")
                    return redirect("signOn")

            email= request.POST["email"]
            if Users.objects.filter(email=email).exists():
                messages.error(request, f"El correo electronico {email} ya existe!")
                return redirect("signOn")

            new_user= Users.objects.create(
                first_name= request.POST["name"],
                last_name= request.POST["last_name"],
                date_birthday= request.POST["date_birthday"],
                rol_user= request.POST["rol"],
                email= email,
                password= request.POST["password1"],
            )
            print("usuario creado")
            return redirect("signIn")
            #tambien le falta una url al que enviarse  
        
        except Exception as e:
            print(f"error al crear usuario: {e}")
            error_message= f"Error al registrar usuario: {e}"
            return render(request, "./login/login.html", {'error_message': error_message})
            #el mensaje de error debe ir en el html de register  
