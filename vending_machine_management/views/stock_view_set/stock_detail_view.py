from rest_framework.generics import RetrieveAPIView

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "id"
