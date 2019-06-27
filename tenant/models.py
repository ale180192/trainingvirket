from django.db import models
from tenant_schemas.models import TenantMixin

class Tenant(TenantMixin):
    name = models.CharField(max_length=128)
    auto_create_schema = True