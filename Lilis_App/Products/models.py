from django.db import models
from Organizations.models import Organization
class BaseModel(models.Model):
    STATES = [
        ("ACTIVE", "Active"),
        ("INACTIVE", "Inactive"),
    ]

    state = models.CharField(max_length=10, choices=STATES, default="ACTIVE")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True
class Products(BaseModel):
    nombre  = models.CharField(max_length=200,unique=True)
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=300)
    tipoProducto = models.CharField(max_length=100)
    stockMinimo = models.FloatField()
    stockMaximo = models.FloatField()
    Organization = models.ForeignKey(Organization, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.nombre
