from django.db import models
from datetime import date
class Users(models.Model):
    ROLES_USER=[
        ("client","Cliente"),
        ("Admin", "Administrador"),
        ("editor", "Editor"),
    ]

    id_user= models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=80, null= False, blank= False)
    last_name= models.CharField(max_length=80, null= False, blank= False)
    date_birthday= models.DateField(null=False, blank= False)
    rol_user= models.CharField(max_length=20, choices=ROLES_USER, null= False, blank= False)
    email= models.EmailField(unique= True, null=False, blank= False)
    password= models.CharField(max_length=120, null=False, blank= False)
    
    assigned_user = models.ManyToManyField("tareas_app.Tasks", related_name="users_assigned_tasks", blank=True, null=True)
    assigned_comment = models.ForeignKey("comments_task.Comments", on_delete=models.CASCADE, blank=True, null= True)


    def calcular_edad(self):
        today= date.today()
        age= today.year - self.date_birthday.year - ((today.month, today.day) < (self.date_birthday.month, self.date_birthday.day))
        return age

    def __str__(self):
        return self.first_name
    
    #buscar como usar el metodo de calcular_edad que ya tenemos, aunque ya el modelo esta