from django.db import models


class Stock(models.Model):
    """Stock model to keep amount of product of each machine."""

    id = models.BigAutoField(primary_key=True)
    machine = models.ForeignKey(to="vending_machine_management.Machine", on_delete=models.CASCADE, null=False)
    product = models.ForeignKey(to="vending_machine_management.Product", on_delete=models.CASCADE, null=False)
    amount = models.PositiveIntegerField(default=0)

    class Meta:
        """Model constraint on duplicate stock instance."""

        constraints = [models.UniqueConstraint(fields=["machine", "product"], name="ux_product_list")]
