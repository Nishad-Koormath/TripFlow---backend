from rest_framework import serializers
from ..payment.models import Payment
import uuid


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ['user', 'transaction_id', 'status', 'created_at']
        
    def create(self, validated_data):
        booking = validated_data['booking']
        amount = booking.total_price
        user = validated_data['user']
        
        transaction_id = str(uuid.uuid4())[:8].upper()
        
        payment = Payment.objects.create(
            booking = booking,
            user = user,
            amount = amount,
            transaction_id = transaction_id,
            status = 'success'
        )
        
        booking.status = 'confirmed'
        booking.save()
        return payment