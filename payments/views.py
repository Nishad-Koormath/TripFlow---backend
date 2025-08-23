from django.shortcuts import render
from rest_framework import permissions, generics
from .models import Payment
from .serializers import PaymentSerializer

# Create your views here.
class PaymentCreateView(generics.CreateAPIView):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]