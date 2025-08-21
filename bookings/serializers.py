from rest_framework import serializers
from .models import Bookings
from catalog.serializers import PackageSerializer
from catalog.models import Package

class BookingSerializer(serializers.ModelSerializer):
    package = PackageSerializer(read_only=True)
    package_id = serializers.PrimaryKeyRelatedField(
        queryset=Package.objects.all(), 
        source="package",
        write_only=True
    )
    
    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ['user', 'total_price', 'created_at']