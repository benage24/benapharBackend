from django.db.models import Sum, F
from django.http import Http404
from django.shortcuts import render
from decimal import Decimal
from datetime import datetime
from rest_framework import status, permissions, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from Caisse.models import DailySales, DailyExpenses
from Caisse.serializers import DailySalesSerializer, DailyExpensesSerializer, DailyProfitsSerializer
from PharmacyInventory.pagination import CustomPageNumberPagination


# Create your views here.




























class DailyReportProfitsList(ListAPIView):
    serializer_class = DailyProfitsSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        # Filter and modify the queryset as needed
        queryset = DailySales.objects.all().order_by('date')
        return queryset

    def list(self, request, *args, **kwargs):
        # Get the filtered and ordered queryset
        queryset = self.filter_queryset(self.get_queryset())
        daily_profits = []
        for sale in queryset:
            daily_profits.append(sale.results)

        # Paginate the data
        page = self.paginate_queryset(daily_profits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        # If not paginated, serialize and return the data
        serializer = self.get_serializer(daily_profits, many=True)
        return Response(serializer.data)


class DailyReportCount(ListAPIView):
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
            daily_profits = []
            for sale in queryset:

                daily_profits.append(sale.results)
            #     # Calculate sums
            total_sum_solde = sum(item["solde"] for item in daily_profits)
            total_sum_sale = sum(item["total_sales"] for item in daily_profits)
            total_sum_profit = sum(item["profit"] for item in daily_profits)
            total_sum_expenses = sum(item["total_expenses"] for item in daily_profits)
            sums = {
                    "total_solde": total_sum_solde,
                    "total_profit": total_sum_profit,
                    "total_expenses": total_sum_expenses,
                    "total_sum_sale": total_sum_sale
                }

            return Response(sums)












class DailyReportProfitsFilter(ListAPIView):
    serializer_class = DailyProfitsSerializer
    pagination_class = CustomPageNumberPagination

    def get_queryset(self):
        # Get the date range from query parameters

        start_date_param = self.request.query_params.get('start_date', None)
        end_date_param = self.request.query_params.get('end_date', None)

        # Convert query parameter strings to datetime objects
        start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
        end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None
        queryset = DailySales.objects.filter_sale_by_date_range(start_date=start_date, end_date=end_date)

        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        daily_profits = []

        for sale in queryset:
            daily_profits.append(sale.results)

        total_sum_solde = sum(item["solde"] for item in daily_profits)
        total_sum_sale = sum(item["total_sales"] for item in daily_profits)
        total_sum_profit = sum(item["profit"] for item in daily_profits)
        total_sum_expenses = sum(item["total_expenses"] for item in daily_profits)
        sums = {
            "total_solde": total_sum_solde,
            "total_profit": total_sum_profit,
            "total_expenses": total_sum_expenses,
            "total_sum_sale": total_sum_sale
        }

        # Serialize the sums along with the daily_profits data
        serializer = self.get_serializer(daily_profits, many=True)
        response_data = {
            "sums": sums,
            "data": serializer.data
        }

        # Paginate the data
        page = self.paginate_queryset(daily_profits)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            response_data["data"] = serializer.data
            return self.get_paginated_response(response_data)

        # If not paginated, return the serialized data and sums
        return Response(response_data)

class SaleViewSet(viewsets.ModelViewSet):
    queryset = DailySales.objects.order_by_date()
    serializer_class = DailySalesSerializer
    pagination_class = CustomPageNumberPagination



# fitler sales by date range
class DailySalesFilterView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Set the pagination class
    serializer_class = DailySalesSerializer

    def get_queryset(self):
        # Get the date range from query parameters

        start_date_param = self.request.query_params.get('start_date', None)
        end_date_param = self.request.query_params.get('end_date', None)

        # Convert query parameter strings to datetime objects
        start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
        end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None
        queryset = DailySales.objects.filter_sale_by_date_range(start_date=start_date, end_date=end_date)

        return queryset

class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = DailyExpenses.objects.order_by_date()
    serializer_class = DailyExpensesSerializer
    pagination_class = CustomPageNumberPagination

# filter expense by date range
class DailyExpenseFilterView(ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPageNumberPagination  # Set the pagination class
    serializer_class =DailyExpensesSerializer

    def get_queryset(self):
        # Get the date range from query parameters

        start_date_param = self.request.query_params.get('start_date', None)
        end_date_param = self.request.query_params.get('end_date', None)

        # Convert query parameter strings to datetime objects
        start_date = datetime.strptime(start_date_param, '%Y-%m-%d') if start_date_param else None
        end_date = datetime.strptime(end_date_param, '%Y-%m-%d') if end_date_param else None
        queryset = DailyExpenses.objects.filter_expense_by_date_range(start_date=start_date,end_date=end_date)

        return queryset