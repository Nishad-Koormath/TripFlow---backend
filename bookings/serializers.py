from rest_framework import serializers
from .models import Bookings

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'
        read_only_fields = ['user', 'status', 'total_price', 'created_at']