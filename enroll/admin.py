from django.contrib import admin
from .models import *


@admin.register(DemoUser)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'password']
