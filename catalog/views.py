from django.shortcuts import render
from rest_framework import generics, filters
from .models import Destination, Category, Package
from .serializers import DestinationSerializer, CategorySerializer, PackageSerializer
from .permissions import IsAdminOrReadOnly

# Create your views here.
class DestinationListView(generics.ListAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'country']
    permission_classes = [IsAdminOrReadOnly]
    
class DestinationDetailView(generics.RetrieveAPIView):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    permission_classes = [IsAdminOrReadOnly]
    
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]

class PackageListView(generics.ListAPIView):
    queryset = Package.objects.filter(is_active=True)
    serializer_class = PackageSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'summary']
    permission_classes = [IsAdminOrReadOnly]

class PackageDetailView(generics.RetrieveAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
    permission_classes = [IsAdminOrReadOnly]
