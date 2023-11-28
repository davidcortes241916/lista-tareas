from django.db import models
from datetime import date

# Create your models here.
class Tasks (models.Model):
    ROLES_VALUE=[
        ("urgente", "Alto"),
        ("importante", "Medio"),
        ("basico", "Bajo"),
    ]

    ROLES_STATE=[
        ("proceso", "En Curso"),
        ("terminado", "Finalizado"),
    ]
    
    id_task= models.AutoField(primary_key=True)
    title= models.CharField(max_length=80, null= False, blank= False)
    description= models.TextField(null=False, blank=False)
    value= models.CharField(max_length=20, choices=ROLES_VALUE, null= False, blank= False)
    state= models.CharField(max_length=20, choices=ROLES_STATE, null= False, blank= False)
    evidence_documents= models.FileField(upload_to= "documents/")
    start_date= models.DateField(null=True, blank=True)
    last_modification= models.DateTimeField(auto_now=True)
    ending_date=  models.DateField(null=True, blank=True)

    assigned_user = models.ForeignKey("user_app.Users", on_delete=models.CASCADE, related_name="tasks_assigned_users")
    assigned_comment= models.ForeignKey("comments_task.Comments", on_delete= models.CASCADE, related_name= "assigned_Task", null= True, blank= True)

    def __str__(self):
        return self.title
