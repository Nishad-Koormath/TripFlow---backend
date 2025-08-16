from django.db import models

# Create your models here.
class Destination(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=100)
    region = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True)
    hero_image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name

class Package(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='packages')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='packages')
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default='INR')
    duration_days = models.PositiveIntegerField()
    summery = models.TextField()
    itinerary_html = models.TextField(blank=True)
    thumbnail = models.ImageField(upload_to='packages/', blank=True, null=True)
    is_active = models.BooleanField(default=True)
    terms_html = models.TextField(blank=True)
    
    def __str__(self):
        return self.title

class PackageMedia(models.Model):
    package = models.ForeignKey(Package, on_delete=models.CASCADE, related_name='media')
    url = models.URLField()
    caption = models.CharField(max_length=200, blank=True)
    order = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return f"{self.package.title} - {self.caption}"
