from django.urls import path
from .views import DailySalesCreateView, DailySalesListView, ExpenseCreateView, DailyExpenseListView, DailyReportProfitsList

urlpatterns = [
    path('sales/create/', DailySalesCreateView.as_view(), name='daily-sales-create'),
    path('sales/list/', DailySalesListView.as_view(), name='daily-sales-list'),
    path('expense/create/', ExpenseCreateView.as_view(), name='expense-daily-create'),
    path('expense/list/', DailyExpenseListView.as_view(), name='expense-daily-list'),
    path('report/', DailyReportProfitsList.as_view(), name='daily-profits-list'),

    # path('expenses/', DailyExpensesList.as_view(), name='daily-expenses-list'),
]
