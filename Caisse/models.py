from django.db import models
from django.db.models import Sum, ExpressionWrapper
from django.db.models import F, Sum, ExpressionWrapper, DecimalField
from decimal import Decimal
from datetime import datetime

class DailyalesManager(models.Manager):
    def order_by_date(self):
        queryset = self.get_queryset().order_by('-date')
        return queryset

    def filter_sale_by_date_range(self, start_date=None, end_date=None):
        queryset = self.get_queryset().order_by('-date')

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset


class DailyExpensesManager(models.Manager):
    def order_by_date(self):
        queryset = self.get_queryset().order_by('-date')
        return queryset

    def filter_expense_by_date_range(self, start_date=None, end_date=None):
        queryset = self.get_queryset().order_by('-date')

        if start_date:
            queryset = queryset.filter(date__gte=start_date)

        if end_date:
            queryset = queryset.filter(date__lte=end_date)

        return queryset


class DailySales(models.Model):
    date = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    objects=DailyalesManager()

    @property
    def total_expenses(self):
        expenses = DailyExpenses.objects.filter(date=self.date).aggregate(total=Sum('amount'))
        return expenses['total'] if expenses['total'] else 0

    @property
    def profit(self):
        return self.amount - self.total_expenses

    @property
    def saving(self):
        return self.profit - self.solde

    @property
    def solde(self):
        return self.profit / Decimal('1.25')
    @property
    def results(self):
        context={
            "date": self.date,
            "total_sales": self.amount,
            "total_expenses": self.total_expenses,
            "profit": self.profit,
            "saving": self.saving,
            "solde": self.solde
        }
        return context


class DailyExpenses(models.Model):
    date = models.DateField()
    description = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now=True)
    objects = DailyExpensesManager()
    @property
    def total_expenses(self):
        return DailyExpenses.objects.filter(date=self.date).aggregate(Sum('amount'))['amount__sum']
