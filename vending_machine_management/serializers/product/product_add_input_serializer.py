from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.product import Product


class ProductAddInputSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
