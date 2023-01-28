from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.product import Product


class ProductSerializer(ModelSerializer):
    """Product model serializer for request and response data."""

    class Meta:
        """Meta data for serializer class.

        See https://www.django-rest-framework.org/api-guide/serializers/#modelserializer for more detail
        """

        model = Product
        fields = "__all__"
