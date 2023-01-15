from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.stock import Stock


class StockInputSerializer(ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"
