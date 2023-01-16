from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer

"""
    API for add stock
    Request format:
    {
        machine: int (machine id),
        product: int (product id),
        amount: int (optional, default is 0)
    }
    See https://www.django-rest-framework.org/api-guide/generic-views/#createapiview for more detail
"""


class StockCreateView(CreateAPIView):
    serializer_class = StockInputSerializer

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        input_serializer = self.serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        try:
            output = input_serializer.save()
        except IntegrityError:
            return Response(
                data={"detail": "Product already exists in this machine"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        output_serializer = StockSerializer(output)
        return Response(data=output_serializer.data, status=status.HTTP_201_CREATED)
