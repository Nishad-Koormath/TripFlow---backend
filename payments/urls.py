from django.urls import path
from .views import PaymentCreateView

urlpatterns = [
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
]