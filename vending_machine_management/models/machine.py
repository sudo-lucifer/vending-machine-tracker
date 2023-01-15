from django.db import models


class Machine(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    location = models.CharField(max_length=100, null=False, blank=False)
