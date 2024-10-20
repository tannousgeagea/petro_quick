from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(ModelAdmin):
    list_display = ('email', 'user_type', 'phone_number', 'business_name', 'vat_number')
    list_filter = ('user_type',)
    search_fields = ('username', 'email', 'business_name', 'vat_number')
    
    unfold = True  # This enables unfolding/collapsible fieldsets
    unfold_fieldsets = [
        ('Account Information', {
            'fields': ['email', 'password'],
        }),
        ('Personal Info', {
            'fields': ['first_name', 'last_name', 'phone_number', 'address'],
        }),
        ('Business Info', {
            'fields': ['business_name', 'vat_number'],
        }),
        ('Permissions', {
            'fields': ['is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'],
        }),
        ('Important Dates', {
            'fields': ['last_login', 'date_joined'],
        }),
    ]