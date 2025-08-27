from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from django.contrib.auth import get_user_model
from users.serializers import UserSerializer
from bookings.models import Bookings
from bookings.serializers import BookingSerializer
from catalog.models import Package, Destination, Category
from catalog.serializers import PackageSerializer, DestinationSerializer, CategorySerializer
from payments.models import Payment
from payments.serializers import PaymentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.db.models import Sum, Count


User = get_user_model()

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and (request.user.is_staff or request.user.is_superuser)
    
@api_view(['GET'])
@permission_classes([IsAdmin])
def dashboard_stats(request):
    total_users = User.objects.count()
    total_bookings = Bookings.objects.count()
    total_revenue = Payment.objects.aggregate(total=Sum('amount'))['total'] or 0
    pending_bookings = Bookings.objects.filter(status='pending').count()
    
    return Response({
        'total_users': total_users,
        'total_bookings': total_bookings,
        'total_revenue': total_revenue,
        'pending_bookings': pending_bookings
    })
    
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]
    
class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAdmin]
    
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAdmin]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdmin]
    
class PaymentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [IsAdmin]
    
class BookingAdminViewSet(viewsets.ModelViewSet):
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdmin]