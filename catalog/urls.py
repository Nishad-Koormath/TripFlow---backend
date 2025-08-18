from django.urls import path
from .views import DestinationListView, DestinationDetailView, CategoryListView, PackageListView, PackageDetailView

urlpatterns = [
    path('destinations/', DestinationListView.as_view(), name='destination-list'),
    path('destinations/<int:pk>/', DestinationDetailView.as_view(), name='destination-detail'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('packages/', PackageListView.as_view(), name='packages-list'),
    path('packages/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
]