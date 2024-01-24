from rest_framework.routers import DefaultRouter

from .views import SheetViewSet
from django.urls import path


router = DefaultRouter()
router.register('upload', SheetViewSet)
urlpatterns = router.urls