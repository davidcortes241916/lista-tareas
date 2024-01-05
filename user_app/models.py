from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from datetime import date

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("El campo de correo electrónico es obligatorio.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, **extra_fields)

class Users(AbstractBaseUser, PermissionsMixin):
    ROLES_USER = [
        ("client", "Cliente"),
        ("Admin", "Administrador"),
        ("editor", "Editor"),
    ]

    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=80, null=False, blank=False)
    last_name = models.CharField(max_length=80, null=False, blank=False)
    date_birthday = models.DateField(null=False, blank=False)
    rol_user = models.CharField(max_length=20, choices=ROLES_USER, null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)
    password = models.CharField(max_length=120, null=False, blank=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    assigned_user = models.ManyToManyField("tareas_app.Tasks", related_name="users_assigned_tasks", blank=True, null=True)
    assigned_comment = models.ForeignKey("comments_task.Comments", on_delete=models.CASCADE, blank=True, null=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'date_birthday', 'rol_user']

    def calcular_edad(self):
        today = date.today()
        age = today.year - self.date_birthday.year - ((today.month, today.day) < (self.date_birthday.month, self.date_birthday.day))
        return age

    def __str__(self):
        return self.first_name
    
    #buscar como usar el metodo de calcular_edad que ya tenemos, aunque ya el modelo esta