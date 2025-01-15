from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class servicee(models.Model):
    SERVICE_CHOICES = [
        ('tv_repair', 'TV Repair'),
        ('laptop_repair', 'Laptop Repair'),
        ('mobile_repair', 'Mobile Repair'),
        ('home_appliances_repair', 'Home Appliances Repair'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name=models.CharField(max_length=122)
    email=models.EmailField()
    phonenumber=models.TextField(max_length=13)
    address=models.TextField(max_length=50)
    city=models.CharField(max_length=10)
    state=models.CharField(max_length=15)
    pincode=models.CharField(max_length=10)
    date=models.DateTimeField()
    service_type=models.CharField(max_length=122,choices=SERVICE_CHOICES)
    
    def __str__(self):
        return f"{self.name}-{self.service_type}"


#reviews model
class rev(models.Model):
    name=models.CharField(max_length=12)
    review=models.TextField()

    def __str__(self):
        return self.name
    
#contact models
class contact(models.Model):
    name=models.CharField(max_length=15)
    email=models.EmailField()
    phone=models.CharField(max_length=13)
    subject=models.CharField(max_length=15)
    message=models.TextField()

    def __str__(self):
        return self.name


