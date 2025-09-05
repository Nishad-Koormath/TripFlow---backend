import razorpay 
from django.conf import settings
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Payment
from .serializers import PaymentSerializer
from bookings.models import Bookings

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    
    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return Payment.objects.all()
        return Payment.objects.filter(user=user)
    
    @action(detail=False, methods=['post'])
    def create_order(self, request):
        booking_id = request.data.get('booking_id')
        booking = Bookings.objects.get(id=booking_id, user=request.user)
        
        amount = int(booking.total_price * 100)
        currency = 'INR'
        
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        order = client.order.create({'amount': amount, 'currency': currency, 'payment_capture': '1'})
        
        payment = Payment.objects.create(
            booking=booking,
            user=request.user,
            amount=booking.total_price,
            currency=currency,
            razorpay_order_id=order['id'],
            status='created',
        )
        return Response({
            "order_id": order["id"],
            "amount": order["amount"],
            "currency": order["currency"],
            "razorpay_key": settings.RAZORPAY_KEY_ID,
            "payment_id": payment.id
        }, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['post'])
    def verify(self, request, pk=None):
        payment = self.get_object()
        data = request.data
        
        client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))
        try:
            client.utility.verify_payment_signature({
                "razorpay_order_id": payment.razorpay_order_id,
                "razorpay_payment_id": data["razorpay_payment_id"],
                "razorpay_signature": data["razorpay_signature"],
            })
            payment.razorpay_payment_id = data["razorpay_payment_id"]
            payment.razorpay_signature = data["razorpay_signature"]
            payment.status = "paid"
            payment.save()
            return Response({"status": "success"}, status=status.HTTP_200_OK)
        except:
            payment.status = "failed"
            payment.save()
            return Response({"status": "failed"}, status=status.HTTP_400_BAD_REQUEST)