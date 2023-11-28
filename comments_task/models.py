from django.db import models
from datetime import date

class Comments(models.Model):
    id_comment= models.AutoField(primary_key=True)
    title= models.CharField(max_length= 40, null= False, blank= False)
    description = models.TextField(null=False, blank=False)
    evidence= models.FileField(upload_to= "documents/", null= True, blank= True)
    qualification= models.IntegerField(null= True, blank=True)
    message_date= models.DateTimeField(auto_now= True)

    assigned_user = models.ForeignKey("user_app.Users", on_delete=models.CASCADE, related_name="comments")
    assigned_task = models.ForeignKey("tareas_app.Tasks", on_delete=models.CASCADE, related_name="comments")


    def __str__(self):
        return self.title
