from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    dashboard_stats, UserViewSet, PackageViewSet,
    DestinationViewSet, CategoryViewSet,
    PaymentViewSet, BookingAdminViewSet
)

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'packages', PackageViewSet)
router.register(r'destinations', DestinationViewSet)
router.register(r'categories', CategoryViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'bookings', BookingAdminViewSet)

urlpatterns = [
    path('dashboard/', dashboard_stats, name='admin-dashboard'),
    path('', include(router.urls)),
]
