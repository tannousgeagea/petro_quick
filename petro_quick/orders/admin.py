from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from .models import Order, OrderItem, FuelType

# Register your models here.
class OrderItemInline(TabularInline):
    model = OrderItem
    fields = ('fuel_type', 'quantity_in_litres', 'cost')
    readonly_fields = ('cost',)  # Display calculated cost as a read-only field
    extra = 1  # Provides one extra blank form for easy item addition

    @admin.display(description='Cost')
    def cost(self, obj):
        return obj.cost
@admin.register(Order)
class OrderAdmin(ModelAdmin):
    list_display = ('id', 'tenant', 'user', 'status', 'order_date', 'estimated_arrival', 'total_cost')
    list_filter = ('status', 'order_date')
    search_fields = ('tenant__tenant_name', 'user__username', 'confirmation_number')
    readonly_fields = ('total_cost',)
    inlines = [OrderItemInline]  # Include the OrderItem inline for managing items in the order

    unfold = True
    unfold_fieldsets = [
        ('Order Information', {
            'fields': ('tenant', 'user', 'order_date', 'status', 'estimated_arrival', 'delivery_address')
        }),
        ('Confirmation', {
            'fields': ('confirmation_number',)
        }),
        ('Cost', {
            'fields': ('total_cost',)
        }),
    ]

    @admin.display(description='Total Cost')
    def total_cost(self, obj):
        return obj.total_cost

@admin.register(FuelType)
class FuelTypeAdmin(ModelAdmin):
    list_display = ('fuel_name', 'price_per_litre')
    search_fields = ('fuel_name',)
    
@admin.register(OrderItem)
class OrderItemAdmin(ModelAdmin):
    list_display = ('order', 'fuel_type', 'cost')

    @admin.display(description='Cost')
    def cost(self, obj):
        return obj.cost