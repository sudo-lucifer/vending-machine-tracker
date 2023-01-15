from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.serializers.product_serializer import ProductSerializer


class StockSerializer(ModelSerializer):
    machine = MachineSerializer(many=False, read_only=True)
    product = ProductSerializer(many=False, read_only=True)

    class Meta:
        model = Stock
        fields = "__all__"
