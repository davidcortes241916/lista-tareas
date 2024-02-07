from django.urls import path
#from django.conf.urls.static import static
from . import views

urlpatterns = [
    path("create/", views.create_Task, name="createTask"),
    path("", views.list_Task, name="listTask"),
]