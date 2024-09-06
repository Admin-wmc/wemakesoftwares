from django.contrib import admin

# Register your models here.

from .models import ConcreteUser

admin.site.register(ConcreteUser)
