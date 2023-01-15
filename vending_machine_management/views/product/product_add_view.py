from django.db import transaction
from rest_framework.generics import CreateAPIView

from vending_machine_management.serializers.product.product_add_input_serializer import ProductAddInputSerializer


class ProductAddView(CreateAPIView):
    serializer_class = ProductAddInputSerializer

    @transaction.atomic
    def perform_create(self, serializer):
        return super().perform_create(serializer)
