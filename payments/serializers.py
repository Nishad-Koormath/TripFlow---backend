from rest_framework import serializers
from .models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
        read_only_fields = ["razorpay_order_id", "razorpay_payment_id", "razorpay_signature", "status", "created_at"]