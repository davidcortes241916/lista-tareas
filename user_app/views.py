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
            print("Intentando crear un nuevo usuario...")
            new_user= Users.objects.create(
                first_name= request.POST["name"],
                last_name= request.POST["last_name"],
                date_birthday= request.POST["date_birthday"],
                rol_user= request.POST["rol"],
                email= request.POST["email"],
                password= request.POST["password1"],
            )
            print("usuario creado exitosamente")
            return redirect("signOn")
            #tambien le falta una url al que enviarse  
        
        except Exception as e:
            print(f"error al registrar: {e}")
            error_message= f"Error al registrar usuario: {e}"
            return render(request, "./login/login.html", {'error_message': error_message})
            #el mensaje de error debe ir en el html de register  
