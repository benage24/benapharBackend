from django.contrib import admin
from .models import DailyExpenses,DailySales
# Register your models here.
admin.site.register(DailyExpenses)
admin.site.register(DailySales)