from rest_framework.generics import DestroyAPIView

from vending_machine_management.models.product import Product

"""
    API to delete product into database
    See https://www.django-rest-framework.org/api-guide/generic-views/#destroyapiview for more detail
    Error handling:
        404 for product does not exist
        204 for delete successfully
"""


class ProductDeleteView(DestroyAPIView):
    queryset = Product.objects.all()
    lookup_field = "id"
