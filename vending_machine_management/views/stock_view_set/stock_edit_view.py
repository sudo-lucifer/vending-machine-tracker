from typing import Dict, Tuple

from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.request import Request
from rest_framework.response import Response

from vending_machine_management.dataclasses.stock_dataclass import StockDataclass
from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockEditView(UpdateAPIView):
    """API for edit stock given by id.

    See https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview for more detail
    """

    queryset = Stock.objects.all()
    serializer_class = StockInputSerializer
    lookup_field = "id"

    @transaction.atomic
    def update(self, request: Request, *args: Tuple[str, str], **kwargs: Dict[str, int]) -> Response:
        """Update, including partial update, existing stock with data from request.

        :param request: Request from client with format
            {
                machine: int (machine id),
                product: int (product id),
                amount: int (optional, default is 0)
            }
        :param args: additional arguments
        :param kwargs: required url parameters
        :return: response with serialized and updated data from stock model
        """
        partial: bool = kwargs.pop('partial', False)
        selected_stock: Stock = self.get_object()
        serializer: StockInputSerializer = self.get_serializer(selected_stock, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        try:
            output: Stock = serializer.save()
        except IntegrityError:
            return Response(
                data={"detail": "Product already exists in this machine"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        output_serializer: StockSerializer = StockSerializer(output)
        response_data: StockDataclass = output_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
