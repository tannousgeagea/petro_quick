
from django.db import models
from users.models import CustomUser

class Tenant(models.Model):
    tenant_id = models.CharField(max_length=255, unique=True)
    tenant_name = models.CharField(max_length=255, unique=True)
    address = models.TextField()
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    vat_number = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tenant'
        verbose_name_plural = "Tenants"

    def __str__(self):
        return self.tenant_name

class TenantUser(models.Model):
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.RESTRICT)
    tenant = models.ForeignKey(Tenant, on_delete=models.RESTRICT, related_name='users')
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='employee')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'tenant_user'
        verbose_name_plural = "Tenant Users"

    def __str__(self):
        return f"{self.user.email} - {self.tenant.tenant_name} ({self.role})"
