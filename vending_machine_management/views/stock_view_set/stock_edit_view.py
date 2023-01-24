from typing import Any, Dict

from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer

"""
    API for edit stock given by Id
    Request format:
    {
        machine: int (machine id),
        product: int (product id),
        amount: int (optional, default is 0)
    }
    See https://www.django-rest-framework.org/api-guide/generic-views/#updateapiview for more detail
"""


class StockEditView(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockInputSerializer
    lookup_field = "id"

    @transaction.atomic
    def update(self, request, *args, **kwargs) -> Response:
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

        if getattr(selected_stock, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            selected_stock._prefetched_objects_cache = {}

        output_serializer: StockSerializer = StockSerializer(output)
        response_data: Dict[str, Any] = output_serializer.data
        return Response(response_data, status=status.HTTP_200_OK)
