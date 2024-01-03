from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Users

# Create your views here.
def formView(request):
    return render(request, "./login/login.html", {})

def loginSignOn(request):
    if request.method != "POST":
       return render(request, "./login/login.html", {})
    else:
        try:
            new_user= Users.objects.create(
                name= request.POST["first_name"],
                last_name= request.POST["last_name"],
                birthday= request.POST["date_birthday"],
                rol= request.POST["rol_user"],
                email= request.POST["email"],
                password= request.POST["password"],
            )
            return render(render, "")
            #tambien le falta una url al que enviarse  
        
        except Exception as e:
            error_message= f"Error al registrar usuario: {e}"
            return render(request, "./login/login.html", {'error_message': error_message})
            #el mensaje de error debe ir en el html de register  

    return render(request, "") 
