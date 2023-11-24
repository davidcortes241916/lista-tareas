from django.db import models
from datetime import date
from user_app.models import Users

# Create your models here.
class Task (models.Model):
    ROLES_VALUE=[
        ("urgente", "Alto"),
        ("importante", "Medio"),
        ("basico", "Bajo"),
    ]

    ROLES_STATE=[
        ("proceso", "En Curso"),
        ("terminado", "Finalizado"),
    ]
    
    id_task= models.IntegerField(unique=True, null= False, blank= False)
    title= models.CharField(max_length=80, null= False, blank= False)
    description= models.TextField(null=False, blank=False)
    value= models.CharField(max_length=20, choices=ROLES_VALUE, null= False, blank= False)
    state= models.CharField(max_length=20, choices=ROLES_STATE, null= False, blank= False)
    evidence_documents= models.FileField(upload_to= "documents/") #crear configuracion
    start_date= models.DateField(null=True, blank=True)
    last_modification= models.DateTimeField(auto_now=True)
    ending_date=  models.DateField(null=True, blank=True)

    assigned_user= models.ForeignKey(Users, on_delete=models.CASCADE)
