from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.serializers.product_serializer import ProductSerializer


class StockSerializer(ModelSerializer):
    """Stock model serializer for response nested data.

    See https://www.django-rest-framework.org/api-guide/serializers/#dealing-with-nested-objects for more detail
    """

    machine = MachineSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        """Meta data for serializer class.

        See https://www.django-rest-framework.org/api-guide/serializers/#modelserializer for more detail
        """

        model = Stock
        fields = "__all__"
