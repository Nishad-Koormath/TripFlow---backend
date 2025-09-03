from django.shortcuts import render
from rest_framework import viewsets, filters
from .models import Destination, Category, Package
from .serializers import DestinationSerializer, CategorySerializer, PackageSerializer
from .permissions import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.
class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
    permission_classes = [IsAdminOrReadOnly]
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class PackageViewSet(viewsets.ModelViewSet):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category', 'destination']
    search_fields = ['title', 'summary']
    permission_classes = [IsAdminOrReadOnly]

