from rest_framework import mixins, viewsets

from vending_machine_management.models.machine import Machine
from vending_machine_management.serializers.machine_serializer import MachineSerializer

"""
    API View set for machine
    Functionality:
        1. Add machine
        2. Edit machine (given product id in url)
        3. Delete machine (given product id in url)
        4. List all machine
        5. Get single machine detail (given product id in url)
    Request format for put (edit machine) and post (create machine) requests:
        {
            name: string,
            location: string
        }
    See https://www.django-rest-framework.org/api-guide/generic-views/#generic-views for more detail
    Remark: this is default by django. You can overwrite function for more complex API functionality i.e filtering,
    pagination result
"""


class MachineViewSet(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer
    http_method_names = ["get", "post", "put", "delete"]
    lookup_field = "id"
