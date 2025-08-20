from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Bookings
from .serializers import BookingSerializer
from .permissions import IsOwnerOrAdmin


# Create your views here.
class BookingViewSet(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    permission_classes = [ IsOwnerOrAdmin]
    
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