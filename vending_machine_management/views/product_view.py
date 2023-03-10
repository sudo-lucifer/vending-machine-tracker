from rest_framework import mixins, viewsets

from vending_machine_management.models.product import Product
from vending_machine_management.serializers.product_serializer import ProductSerializer


class ProductViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """API View set for product.

    Functionality:
        1. Add product
        2. Edit product (given product id in url)
        3. Delete product (given product id in url)
        4. List all products
        5. Get single product detail (given product id in url)
    Request format for put (edit product) and post (create product) requests:
        {
            name: string,
            price: decimal number (optional)
        }
    See https://www.django-rest-framework.org/api-guide/generic-views/#generic-views for more detail
    Remark: this is default by django. You can overwrite function for more complex API functionality i.e filtering,
    pagination result
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ["get", "post", "put", "delete"]
    lookup_field = "id"
