from django.db import models
from users.models import CustomUser

class FuelType(models.Model):
    fuel_name = models.CharField(max_length=50)
    price_per_litre = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.fuel_name} - {self.price_per_litre}/L"

class Order(models.Model):
    ORDER_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    fuel_type = models.ForeignKey(FuelType, on_delete=models.PROTECT)
    quantity_in_litres = models.DecimalField(max_digits=5, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='pending')
    delivery_address = models.TextField(blank=False, null=False)
    estimated_arrival = models.DateTimeField(blank=True, null=True)
    confirmation_number = models.CharField(max_length=255, blank=True, null=True, unique=True)

    def __str__(self):
        return f"Order {self.pk} by {self.user} - {self.status}"
