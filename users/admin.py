from django.contrib import admin
from .models import User, Role, CustomPermission, Module

# Register your models here.
admin.site.register(User)
admin.site.register(Role)
admin.site.register(Module)
admin.site.register(CustomPermission)