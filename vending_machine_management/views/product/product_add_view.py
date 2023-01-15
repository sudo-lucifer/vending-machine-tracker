from django.db import transaction
from rest_framework.generics import CreateAPIView

from vending_machine_management.serializers.product.product_serializer import ProductSerializer

"""
    API to add product into database
    Request format:
    {
        name: string,
        price: decimal number
    }
    attribute name is required, but price is 0.0 br default (if not given by user)
"""


class ProductAddView(CreateAPIView):
    serializer_class = ProductSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        return super().perform_create(serializer)
