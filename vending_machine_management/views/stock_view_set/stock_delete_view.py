from rest_framework.generics import DestroyAPIView

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer


class StockDeleteView(DestroyAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockInputSerializer
    lookup_field = "id"
