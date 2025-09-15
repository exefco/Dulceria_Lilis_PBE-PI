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

class Rol(BaseModel):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


class Usuario(BaseModel):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE, null=True, blank=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.nombre


