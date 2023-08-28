from rest_framework.routers import DefaultRouter

from .views import  ProductViewSet
from django.urls import path


router = DefaultRouter()
router.register('product', ProductViewSet)
urlpatterns = router.urls
# urlpatterns = [
#     path('list/', ProductListView.as_view()),
#     path('create/', ProductCreateView.as_view()),
#         path('<int:pk>/', ProductDetail.as_view()),
#     path('delete/<int:pk>/', ProductDelete.as_view()),
#     path('update/<int:pk>/', ProductUpdate.as_view()),
#
# ]