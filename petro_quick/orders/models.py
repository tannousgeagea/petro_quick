from django.db import models
from users.models import CustomUser
from tenants.models import Tenant

class FuelType(models.Model):
    fuel_name = models.CharField(max_length=50)
    price_per_litre = models.DecimalField(max_digits=6, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'fuel_type'
        verbose_name_plural = "Fuel Types"

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

    tenant = models.ForeignKey(Tenant, on_delete=models.RESTRICT, related_name='orders')
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True, blank=True, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=ORDER_STATUS_CHOICES, default='pending')
    delivery_address = models.TextField(blank=False, null=False)
    estimated_arrival = models.DateTimeField(blank=True, null=True)
    confirmation_number = models.CharField(max_length=255, blank=True, null=True, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = 'order'
        verbose_name_plural = "Orders"

    def __str__(self):
        return f"Order {self.pk} by {self.user} - {self.status}"

    @property
    def total_cost(self):
        return sum(item.cost for item in self.order_items.all())

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_items')
    fuel_type = models.ForeignKey(FuelType, on_delete=models.PROTECT)
    quantity_in_litres = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'order_item'
        verbose_name_plural = "Order Items"

    def __str__(self):
        return f"{self.quantity_in_litres}L of {self.fuel_type.fuel_name} for Order {self.order.pk}"

    @property
    def cost(self):
        return self.quantity_in_litres * self.fuel_type.price_per_litre
    
class OrderStatusHistory(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="status_history")
    status = models.CharField(max_length=10, choices=Order.ORDER_STATUS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)  # User updating the status

    def __str__(self):
        return f"{self.status} at {self.timestamp}"
