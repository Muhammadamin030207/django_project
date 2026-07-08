from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    role=models.CharField(max_length=10, choices=[('admin', 'Admin'), ('user', 'User')], default='user')