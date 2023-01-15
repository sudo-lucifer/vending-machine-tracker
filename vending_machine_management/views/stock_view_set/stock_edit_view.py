from django.db import IntegrityError, transaction
from rest_framework import status
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response

from vending_machine_management.models.stock import Stock
from vending_machine_management.serializers.stock.stock_input_serializer import StockInputSerializer
from vending_machine_management.serializers.stock.stock_serializer import StockSerializer


class StockEditView(UpdateAPIView):
    queryset = Stock.objects.all()
    serializer_class = StockInputSerializer
    lookup_field = "id"

    @transaction.atomic
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        try:
            output = serializer.save()
        except IntegrityError:
            return Response(
                data={"detail": "Product already exists in this machine"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # forcibly invalidate the prefetch cache on the instance.
            instance._prefetched_objects_cache = {}

        output = StockSerializer(output)
        return Response(output.data, status=status.HTTP_200_OK)
