from django.db.models import Sum, F
from django.http import Http404
from django.shortcuts import render
from decimal import Decimal

from rest_framework import status, permissions
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Caisse.models import DailySales, DailyExpenses
from Caisse.serializers import DailySalesSerializer, DailyExpensesSerializer, DailyProfitsSerializer
from PharmacyInventory.pagination import CustomPageNumberPagination


# Create your views here.
def get_DailySales_object(pk):
    try:
        return DailySales.objects.get(pk=pk)
    except DailySales.DoesNotExist:
        raise Http404

def get_ExpenseSales_object(pk):
    try:
        return DailyExpenses.objects.get(pk=pk)
    except DailySales.DoesNotExist:
        raise Http404


class DailySalesCreateView(APIView):
    serializer_class = DailySalesSerializer
    def post(self, request, format=None):
        serializer = DailySalesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class DailySalesListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Set the pagination class
    serializer_class = DailySalesSerializer

    def get_queryset(self):
        # Customize your queryset here
        queryset = DailySales.objects.order_by('date')
        return queryset
    # def get(self, request, format=None):
    #     snippets = DailySales.objects.all().order_by('date')
    #     serializer = DailySalesSerializer(snippets, many=True)
    #
    #     return Response(serializer.data)




class DailySalesDelete(APIView):

    def delete(self, request, pk, format=None):
        snippet = get_DailySales_object(pk)
        print(snippet)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class ExpenseCreateView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    serializer_class = DailyExpensesSerializer
    def post(self, request, format=None):
        serializer = DailyExpensesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class DailyExpenseListView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class =DailyExpensesSerializer
    pagination_class = CustomPageNumberPagination  # Set the pagination class

    def get_queryset(self):
        # Customize your queryset here
        queryset = DailyExpenses.objects.order_by('date')
        return queryset




class DailyExpenseDelete(APIView):

    def delete(self, request, pk, format=None):
        snippet = get_ExpenseSales_object(pk)
        print(snippet)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class DailyReportProfitsList(ListAPIView):
    serializer_class = DailyProfitsSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        # Filter and modify the queryset as needed
        daily_expenses = DailyExpenses.objects.all().order_by('date')
        queryset = DailySales.objects.all().order_by('date')

        return queryset

    def list(self, request, *args, **kwargs):
        # Get the filtered and ordered queryset
        queryset = self.filter_queryset(self.get_queryset())
        daily_expenses = DailyExpenses.objects.all().order_by('date')

        daily_profits = []
        for sale in queryset:
            total_sales = sale.amount
            total_expenses = sum(expense.amount for expense in daily_expenses if expense.date == sale.date)
            profit = sale.amount - total_expenses
            res = profit / Decimal('1.25')

            saving = profit - res

            daily_profits.append({
                "date": sale.date,
                "total_sales": total_sales,
                "total_expenses": total_expenses,
                "profit": profit,
                "saving": saving,
                "solde": res
            })

        # Paginate the data
        page = self.paginate_queryset(daily_profits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If not paginated, serialize and return the data
        serializer = self.get_serializer(daily_profits, many=True)
        return Response(serializer.data)





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