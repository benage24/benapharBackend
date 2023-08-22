from django.db.models import Sum, F
from django.http import Http404
from django.shortcuts import render
from decimal import Decimal

from rest_framework import status, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Caisse.models import DailySales, DailyExpenses
from Caisse.serializers import DailySalesSerializer, DailyExpensesSerializer
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



class DailySalesListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Set the pagination class

    def get(self, request, format=None):
        snippets = DailySales.objects.all()
        serializer = DailySalesSerializer(snippets, many=True)

        return Response(serializer.data)




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




class DailyExpenseListView(APIView):
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, format=None):
        snippets = DailyExpenses.objects.all()
        serializer = DailyExpensesSerializer(snippets, many=True)

        return Response(serializer.data)


class DailyExpenseDelete(APIView):

    def delete(self, request, pk, format=None):
        snippet = get_ExpenseSales_object(pk)
        print(snippet)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class DailyReportProfitsList(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Set the pagination class

    def get(self, request):
        daily_sales = DailySales.objects.all()
        daily_expenses = DailyExpenses.objects.all()

        # Paginate manually
        page = self.request.query_params.get('page')
        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')

        if page and limit:
            limit = int(limit)
            offset = int(offset) if offset else 0
            start_index = offset + (limit * (int(page) - 1))
            end_index = start_index + limit
            daily_sales = daily_sales[start_index:end_index]

        daily_profits = []
        for sale in daily_sales:
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
                "saving": saving
            })

        return Response(daily_profits)

# class DailyReportProfitsList(APIView):
#     # permission_classes = [permissions.IsAuthenticated]
#     pagination_class = LimitOffsetPagination
#     def get(self, request):
#         daily_sales = DailySales.objects.all()
#         daily_expenses = DailyExpenses.objects.all()
#
#         daily_profits = []
#         for sale in daily_sales:
#             total_sales = sale.amount
#             total_expenses = sum(expense.amount for expense in daily_expenses if expense.date == sale.date)
#             profit = sale.amount - total_expenses
#             res= profit/Decimal('1.25')
#             saving=profit-res
#             print(res)
#
#             daily_profits.append({
#                 "date": sale.date,
#                 "total_sales": total_sales,
#                 "total_expenses": total_expenses,
#                 "profit": profit,
#                 "saving":saving
#             })
#
#         return Response(daily_profits)
#

class ProductListView(APIView):
    # permission_classes = [permissions.IsAuthenticated]
    pagination_class = LimitOffsetPagination  # Set the pagination class

    def get(self, request, format=None):
        snippets = DailySales.objects.all()

        # Create an instance of the pagination class
        paginator = self.pagination_class()

        # Paginate manually
        page = self.request.query_params.get('page')
        limit = self.request.query_params.get('limit')
        offset = self.request.query_params.get('offset')

        if page and limit:
            self.pagination_class.page_size = int(limit)  # Adjust page size
            page_number = int(page)
            paginated_data = paginator.paginate_queryset(snippets, self.request)
            serializer = DailySalesSerializer(paginated_data, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = DailySalesSerializer(snippets, many=True)
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