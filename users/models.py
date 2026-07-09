from django.contrib.auth.models import AbstractUser
from django.db import models
from rest_framework.exceptions import ValidationError
class User(AbstractUser):
    role=models.CharField(max_length=20, choices=[('admin', 'Admin'),('seller', 'Seller'),('super_admin','Super_Admin'), ('user', 'User')], default='super_admin')
    
    def save(self, *args, **kwargs):
        if self.role == "super_admin":
            if User.objects.filter(role="super_admin").exclude(id=self.id).exists():
                raise ValidationError(
                    "Projectda faqat bitta super_admin bo'lishi mumkin."
                )

        super().save(*args, **kwargs)