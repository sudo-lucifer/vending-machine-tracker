from rest_framework.generics import DestroyAPIView

from vending_machine_management.models.stock import Stock

"""
    API for delete stock given by id
    See https://www.django-rest-framework.org/api-guide/generic-views/#destroyapiview for more detail
    Remark: this is default by django. You can overwrite function for more complex API functionality i.e filtering,
    pagination result
"""


class StockDeleteView(DestroyAPIView):
    queryset = Stock.objects.all()
    lookup_field = "id"
