from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline, StackedInline
from tenants.models import (
    Tenant,
    TenantUser
)

# Register your models here.
@admin.register(Tenant)
class TenantAdmin(ModelAdmin):
    list_display = ("tenant_id", "tenant_name", "contact_phone", "contact_email")
    list_filters = ('created_at')
    search_fields = ('tenant_id', 'tenant_name')
    
@admin.register(TenantUser)
class TenantUserAdmin(ModelAdmin):
    list_display = ('tenant', 'user', 'role', 'created_at')
    list_filter = ('tenant__tenant_name', 'role')
    search_display = ('user__email')