from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    class Roles(models.TextChoices):
        VISITOR = 'visitor', 'Visitor'
        CUSTOMER = 'customer', 'Customer'
        STAFF = 'staff', 'Staff'
        ADMIN = 'admin', 'Admin'
        
    role = models.CharField(max_length=20, choices=Roles.choices, default=Roles.CUSTOMER)
    phone = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.username