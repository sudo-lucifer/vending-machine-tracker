from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.stock import Stock


class StockInputSerializer(ModelSerializer):
    """Stock model serializer for request data."""

    class Meta:
        """Meta data for serializer class.

        See https://www.django-rest-framework.org/api-guide/serializers/#modelserializer for more detail
        """

        model = Stock
        fields = "__all__"
