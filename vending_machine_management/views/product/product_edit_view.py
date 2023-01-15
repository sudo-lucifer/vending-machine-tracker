from rest_framework.generics import UpdateAPIView

from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer

"""
    API to edit product into database
    See https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview for more detail
    Request format:
    {
        name: string,
        price: decimal number
    }
    attribute name is required, but price is optional field (will not edit if not given by user)
    product id is required and need to put in API url (See file url.py)
    Error handling:
        400 for duplicate product name
        404 for product does not exist
"""


class ProductEditView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "id"
