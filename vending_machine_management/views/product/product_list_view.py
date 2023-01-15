from rest_framework.generics import ListAPIView

from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer

"""
    API to list all products available in the system
    ListAPIView is default from django rest framework
    See https://www.django-rest-framework.org/api-guide/generic-views/#listapiview for more detail
"""


class ProductListView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
