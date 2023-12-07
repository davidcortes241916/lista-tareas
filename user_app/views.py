from django.shortcuts import render

# Create your views here.
def formView(request):
    return render(request, "./login/login.html", {})
