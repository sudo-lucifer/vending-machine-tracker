from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from rest_framework.views import APIView

from vending_machine_management.dataclasses.product.product_edit_dataclass import ProductEditDataclass
from vending_machine_management.serializers.product.product_edit_input_serializer import ProductEditInputSerializer
from vending_machine_management.serializers.product.product_serializer import ProductSerializer
from vending_machine_management.services.product.product_edit_service import ProductEditService

"""
    API to edit product into database
    Request format:
    {
        name: string,
        price: decimal number
    }
    attribute name is required, but price is 0.0 br default (if not given by user)
    product id is required and need to put in API url (See file url.py)
    Error handling:
        500 for duplicate product name
        404 for product does not exist
"""


class ProductEditView(APIView):
    def put(self, request, product_id: int):
        input_serializer = ProductEditInputSerializer(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        input_data: ProductEditDataclass = input_serializer.validated_data
        try:
            new_product = ProductEditService.edit_product(product_id, input_data)
        except IntegrityError:
            return Response(
                data={"detail": f"Name '{input_data.name}' already exists"}, status=HTTP_500_INTERNAL_SERVER_ERROR
            )
        if new_product is None:
            return Response(data={"detail": f"Not found product id {product_id}"}, status=HTTP_404_NOT_FOUND)
        output_serializer = ProductSerializer(new_product)
        return Response(data=output_serializer.data, status=HTTP_200_OK)