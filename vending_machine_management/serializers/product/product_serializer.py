from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.product import Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
