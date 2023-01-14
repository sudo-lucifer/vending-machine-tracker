from rest_framework.generics import ListAPIView
from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.product import Product

"""
    API response formatter for product list API
    See https://www.django-rest-framework.org/api-guide/serializers/#modelserializer for more detail
"""


class ProductListOutputSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


"""
    API to list all products available in the system
    ListAPIView is default from django rest framework
    See https://www.django-rest-framework.org/api-guide/generic-views/#listapiview for more detail
"""


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListOutputSerializer
