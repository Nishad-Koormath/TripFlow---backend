from rest_framework import serializers
from .models import Destination, Category, Package, PackageMedia

class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destination
        fields = '__all__'
        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PackageMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageMedia
        fields = '__all__'
    
class PackageSerializer(serializers.ModelSerializer):
    destination = serializers.PrimaryKeyRelatedField(
        queryset=Destination.objects.all()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all()
    )
    media = PackageMediaSerializer(many=True, read_only=True)
    thumbnail = serializers.ImageField(use_url=True)
    
    class Meta:
        model = Package
        fields = '__all__'