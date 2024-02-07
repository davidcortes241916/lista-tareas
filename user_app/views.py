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

def loginB(request):
    return render(request, "./login/signIn.html", {})

def loginSignOn(request):
    if request.method != "POST":
       return render(request, "./login/login.html", {}) 
        #aqui se busca por defecto que el formulario envie los datos como POST
        #pues se redirecciona al login
    else:
        if "cancelar" in request.POST:
            return redirect("signIn")
            #es solo una opcionen caso de que el usuario presione el boton de cancelar
            # si es asi redirecciona al inicio de sesion

        try: #aqui usamos try para evitar errores
            #quitar los prints cuando esto funcione bien
            print("intentando crear usuario")
            required_fields = ["name", "last_name", "date_birthday", "rol", "email", "password1"]
            #la linea 32 hace que los campos sean obligatorios 

            for field in required_fields:  
                if not request.POST.get(field):
                    print("todos los campos son necesarios")
                    messages.error(request, "Debe completar todos los campos!")
                    return redirect("signOn")
                #es un mensaje de error, en caso de que el usuario no complete
                #los campos, donde se redirecciona al registro normalmente

            email= request.POST["email"] #toma el email para validarlo
            if Users.objects.filter(email=email).exists():
                #busca los valores de email en la bd
                #donde busca que no este repetido, que no exiista, porque si existe
                #entonces::
                print("correo ya existe")
                messages.error(request, f"El correo electronico {email} ya existe!")
                return redirect("signOn") #devuelve un error y de nuevo redireccion 
                #al registro

            user= Users.objects.create_user( #crea el resto de los datos
                first_name= request.POST["name"],
                last_name= request.POST["last_name"],
                date_birthday= request.POST["date_birthday"],
                rol_user= request.POST["rol"],
                email= email, #aqui solo se llama el campo de email que se creo ates
                password= request.POST["password1"],
            )
            user.is_active= True #valida si el usuario esta creado
            user.save() #guarda el usuario
            print("usuario creado")
            return redirect("signIn")
            #tambien le falta una url al que enviarse  
        
        except Exception as e: #solo es en caso de que haya ocurrido un error
            print(f"error al crear usuario: {e}")
            close_old_connections() #cierra la conexion de la BD
            error_message= f"Error al registrar usuario: {e}"
            return render(request, "./login/login.html", {'error_message': error_message})    

def loginSignIn(request):

    if request.method != "POST": #valida que si sea el formulario de tipo POST
        return render(request, "./login/signIn.html", {})
    else:
        #toma los valores creados de email y password
        email = request.POST["email"]
        password = request.POST["password1"]
        
        try:
            user = authenticate(request, email=email, password=password)
            #user valida y autentica que si esten creados los campos de password y email
            #en el mismo id
            print(user)
            if user is not None and user.is_active:
                #valida si el usuario esta activado en la BD
                login(request, user) #login es una libreria que permite el acceso
                return redirect("home/") #redirecciona al index
            else:
                print("Usuario no activo") #el error afirma que no esta activo por
                #contraseña y/o correo
                messages.error(request, "Correo o contraseña incorrectos!")
                return render(request, "./login/signIn.html", {})#redirecciona normalmente
                #al inicio de sesion
        except ValidationError as e:
            print("Error de validación:", e) #en caso de errores, es casi lo mismo pero
            #con except para poder cerrarlo
            messages.error(request, "Correo o contraseña incorrectos!")
            return render(request, "./login/signIn.html", {})
    
def signout(request): #se arreglo cambiando el nombre del metodo
    logout(request) #lo que hace es que logout desactiva la cuenta para 
    #cerrar la sesion y que tenga que iniciar de nuevo
    return redirect("signIn") 