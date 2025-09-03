from django.urls import path, include
from .views import DestinationViewSet, CategoryViewSet, PackageViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'destinations', DestinationViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'packages', PackageViewSet)
urlpatterns = [
    path('', include(router.urls)),
]