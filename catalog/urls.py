from django.urls import path
from .views import DestinationListView, CategoryListView, PackageListView, PackageDetailView

urlpatterns = [
    path('destinations/', DestinationListView.as_view(), name='destinations'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('packages/', PackageListView.as_view(), name='packages'),
    path('packages/<int:pk>/', PackageDetailView.as_view(), name='package-detail'),
]