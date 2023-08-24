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

class DailyProfitsSerializer(serializers.Serializer):
    date = serializers.DateField()
    total_sales = serializers.DecimalField(max_digits=10, decimal_places=2)
    total_expenses = serializers.DecimalField(max_digits=10, decimal_places=2)
    profit = serializers.DecimalField(max_digits=10, decimal_places=2)
    saving = serializers.DecimalField(max_digits=10, decimal_places=2)
    solde = serializers.DecimalField(max_digits=10, decimal_places=2)
