from rest_framework.generics import RetrieveAPIView

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer

"""
    API for get detail for stock given by id
    See https://www.django-rest-framework.org/api-guide/generic-views/#retrieveapiview for more detail
    Remark: this is default by django. You can overwrite function for more complex API functionality i.e filtering,
    pagination result
"""


class StockDetailView(RetrieveAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    lookup_field = "id"
