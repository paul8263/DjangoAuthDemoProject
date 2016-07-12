from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.DEUserProfile)
class DEUserAdmin(admin.ModelAdmin):
    pass
