from django.urls import path
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("signOn/", views.loginSignOn, name="signOn"),
    path("signIn/", views.formView, name= "signIn")
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
