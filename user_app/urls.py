from django.urls import path, include
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("signOn/", views.loginSignOn, name="signOn"),
    path("login/", views.loginSignIn, name= "signIn"),
    path("", include("tareas_app.urls")),
    path("logout/", views.signout, name="logout"),
    path("/", views.loginB, name="login"),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
