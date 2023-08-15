from django.db import models
from django.db.models import Sum


class DailySales(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)

class DailyExpenses(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    @property
    def total_expenses(self):
        return DailyExpenses.objects.filter(date=self.date).aggregate(Sum('amount'))['amount__sum']
