from typing import Dict, Tuple

from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from vending_machine_management.dataclasses.stock_dataclass import StockDataclass
from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockCreateView(CreateAPIView):
    """API for add stock.

    See https://www.django-rest-framework.org/api-guide/generic-views/#createapiview for more detail
    """

    serializer_class = StockInputSerializer

    @transaction.atomic
    def create(self, request: Request, *args: Tuple[str, str], **kwargs: Dict[str, int]) -> Response:
        """Insert request stock data to database.

        :param request: Request from user with format
            {
                machine: int (machine id),
                product: int (product id),
                amount: int (optional, default is 0)
            }
        :param args: additional arguments
        :param kwargs: required variable in url
        :return: response with serialized data from stock model
        """
        input_serializer: StockInputSerializer = self.serializer_class(data=request.data)
        input_serializer.is_valid(raise_exception=True)
        try:
            output: Stock = input_serializer.save()
        except IntegrityError:
            return Response(
                data={"detail": "Product already exists in this machine"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        output_serializer: StockSerializer = StockSerializer(output)
        response_data: StockDataclass = output_serializer.data
        return Response(data=response_data, status=status.HTTP_201_CREATED)
