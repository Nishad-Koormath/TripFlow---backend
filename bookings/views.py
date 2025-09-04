from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Bookings
from .serializers import BookingSerializer
from .permissions import IsOwnerOrAdmin
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [ IsOwnerOrAdmin]
    
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'travel_date', 'package']  
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Bookings.objects.all()
        return Bookings.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        package = serializer.validated_data['package']
        num_people = serializer.validated_data['num_people']
        total_price = package.base_price * num_people
        serializer.save(user=self.request.user, total_price=total_price)

    @action(detail=True, methods=['patch'], permission_classes=[IsOwnerOrAdmin])
    def cancel(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'pending':
            return Response(
                {"error": "Only pending bookings can be cancelled."},
                status=status.HTTP_400_BAD_REQUEST
            )
        booking.status = "cancelled"
        booking.save()
        return Response(BookingSerializer(booking).data, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['patch'], permission_classes=[permissions.IsAdminUser])
    def confirm(self, request, pk=None):
        booking = self.get_object()
        if booking.status != 'pending':
            return Response(
                {"error": "Only pending bookings can be confirmed."},
                status=status.HTTP_400_BAD_REQUEST
            )
        booking.status = "confirmed"
        booking.save()
        return Response(BookingSerializer(booking).data, status=status.HTTP_200_OK)