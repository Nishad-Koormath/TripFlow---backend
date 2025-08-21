from rest_framework import serializers
from .models import Bookings
from catalog.serializers import PackageSerializer

class BookingSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True)
    
    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ['user', 'status', 'total_price', 'created_at']