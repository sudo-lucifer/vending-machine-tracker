from rest_framework.generics import ListAPIView

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockListView(ListAPIView):
    """API for list all available stocks on every machine.

    See https://www.django-rest-framework.org/api-guide/generic-views/#listapiview for more detail
    Remark: this is default by django. You can overwrite function for more complex API functionality i.e filtering,
    pagination result
    """

    queryset = Stock.objects.all()
    serializer_class = StockSerializer
