from django.db import models
from category.models import Category
# Create your models here.
class SubCategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,related_name='subcategories')
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f'{self.category.name} - {self.name}'