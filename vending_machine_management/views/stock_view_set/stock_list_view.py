from rest_framework.generics import ListAPIView

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockListView(ListAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
