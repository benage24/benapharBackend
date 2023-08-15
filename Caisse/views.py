from django.db.models import Sum, F
from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView

from Caisse.models import DailySales, DailyExpenses
from Caisse.serializers import DailySalesSerializer, DailyExpensesSerializer


# Create your views here.


class DailySalesCreateView(APIView):
    serializer_class = DailySalesSerializer
    def post(self, request, format=None):
        serializer = DailySalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DailySalesListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        snippets = DailySales.objects.all()
        serializer = DailySalesSerializer(snippets, many=True)

        return Response(serializer.data)


class ExpenseCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DailyExpensesSerializer
    def post(self, request, format=None):
        serializer = DailyExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DailyExpenseListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request, format=None):
        snippets = DailyExpenses.objects.all()
        serializer = DailyExpensesSerializer(snippets, many=True)

        return Response(serializer.data)





class DailyReportProfitsList(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        daily_sales = DailySales.objects.all()
        daily_expenses = DailyExpenses.objects.all()

        daily_profits = []
        for sale in daily_sales:
            total_sales = sale.amount
            total_expenses = sum(expense.amount for expense in daily_expenses if expense.date == sale.date)
            profit = sale.amount - total_expenses

            daily_profits.append({
                "date": sale.date,
                "total_sales": total_sales,
                "total_expenses": total_expenses,
                "profit": profit
            })

        return Response(daily_profits)


# class DailyReportProfitsList(APIView):
#     def get(self, request):
#         # Annotate the DailySales queryset with aggregated data
#         daily_data = DailySales.objects.annotate(
#             # Calculate the total sales for each day using Sum aggregation
#             total_sales=Sum('amount'),
#
#             # Calculate the total expenses for each day using Sum aggregation and filtering
#             # Filter the expenses to consider only those with the same date as the sales entry
#             total_expenses=Sum('amount', filter=F('amount')),
#         ).values('date', 'total_sales', 'total_expenses')
#
#         # Return the calculated data as a JSON response using Response class
#         return Response(daily_data)