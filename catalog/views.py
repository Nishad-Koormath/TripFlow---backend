from django.shortcuts import render
from rest_framework import generics, filters
from .models import Destination, Category, Package
from .serializers import DestinationSerializer, CategorySerializer, PackageSerializer

# Create your views here.
class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class PackageListView(generics.ListAPIView):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'summary']

class PackageDetailView(generics.ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
