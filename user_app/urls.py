from django.urls import path
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("signOn/", views.loginSignOn, name="signOn"),
    path("", views.loginSignIn, name= "signIn"),
    path("home/", views.home, name="home")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
