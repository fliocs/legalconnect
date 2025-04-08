from django.contrib import admin
from .models import Client
# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'telephone', 'adresse')
    search_fields = ('client__user__email', 'client__user__last_name')
    list_select_related = ('user',)  # Optimise les requêtes SQL



