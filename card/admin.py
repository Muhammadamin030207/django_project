from django.contrib import admin
from .models import Card


@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity', 'created_at']
    list_filter = ['user', 'created_at']
    search_fields = ['user__username', 'product__name']
