from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import DailyExpenseFilterView, DailyReportCount, DailySalesFilterView, \
    DailyReportProfitsFilter, \
     DailyReportProfitsList, SaleViewSet, ExpenseViewSet

router = DefaultRouter()
router.register('sales', SaleViewSet)
router.register('expense', ExpenseViewSet)
# urlpatterns = router.urls
urlpatterns = [

    path('report/', DailyReportProfitsList.as_view(), name='daily-profits-list'),


    #filter
    path('report/filter/', DailyReportProfitsFilter.as_view(), name='daily-profits-list'),
    path('sales/filter/', DailySalesFilterView.as_view(), name='daily-profits-list'),
    path('expense/filter/', DailyExpenseFilterView.as_view(), name='daily-profits-list'),

    path('report/count/', DailyReportCount.as_view(), name='daily-profits-list'),

    # path('expenses/', DailyExpensesList.as_view(), name='daily-expenses-list'),
] + router.urls
