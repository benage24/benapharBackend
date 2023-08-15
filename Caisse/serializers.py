from rest_framework import serializers
from .models import DailySales, DailyExpenses

class DailySalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySales
        fields = '__all__'

class DailyExpensesSerializer(serializers.ModelSerializer):
    total_expenses = serializers.ReadOnlyField()

    class Meta:
        model = DailyExpenses
        fields = '__all__'
