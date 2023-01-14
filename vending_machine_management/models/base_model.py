from django.db import models
from rest_framework import status
from rest_framework.exceptions import APIException


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class NotFoundAPIException(APIException):
        status_code = status.HTTP_404_NOT_FOUND
        default_code = 'Not found'
        default_detail = 'Not such item'

    class Meta:
        abstract = True
