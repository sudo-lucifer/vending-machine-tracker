from django.urls import path

from vending_machine_management.views.machine_view import MachineViewSet

machine_urls = [
    path(
        "<int:id>",
        MachineViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy',
            }
        ),
        name='retrieve-update-destroy',
    ),
    path(
        "list-create",
        MachineViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='list-create',
    ),
]
