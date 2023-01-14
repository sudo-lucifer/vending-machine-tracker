from django.db import models

from vending_machine_management.models.base_model import BaseModel

# Create your models here.


class VendingMachine(BaseModel):
    id = models.BigAutoField(primary_key=True)
    machine_name = models.CharField(max_length=100, null=False, blank=False)
    location = models.CharField(max_length=100, null=False, blank=False)
