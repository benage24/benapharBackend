from django.db import models

# Create your models here.
class DailyFinancialRecord(models.Model):
    date = models.DateField()
    total_sales = models.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = models.DecimalField(max_digits=10, decimal_places=2)


    @property
    def total(self):
        return self.total_sales - self.total_expenses