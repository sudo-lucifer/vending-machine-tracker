from django.core.validators import MinValueValidator
from django.db import models


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    price = models.FloatField(default=0.0, validators=[MinValueValidator(0.0)])
