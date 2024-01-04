from django.urls import path
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("", views.loginSignOn, name="signOn"),
]

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
