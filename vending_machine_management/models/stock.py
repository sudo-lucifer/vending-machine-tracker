from django.db import models

from vending_machine_management.models.base_model import BaseModel

# Create your models here.


class Stock(BaseModel):
    id = models.BigAutoField(primary_key=True)
    vending_machine = models.ForeignKey(to="vending_machine_management.Machine", on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(to="vending_machine_management.Product", on_delete=models.CASCADE, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
