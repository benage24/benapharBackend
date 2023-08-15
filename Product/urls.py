from .views import ProductListView,ProductCreateView,ProductDetail,ProductDelete,ProductUpdate
from django.urls import path

urlpatterns = [
    path('list/', ProductListView.as_view()),
    path('create/', ProductCreateView.as_view()),
        path('<int:pk>/', ProductDetail.as_view()),
    path('delete/<int:pk>/', ProductDelete.as_view()),
    path('update/<int:pk>/', ProductUpdate.as_view()),

]