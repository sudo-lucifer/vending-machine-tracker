from django.urls import path

from vending_machine_management.views.product_view import ProductViewSet

product_urls = [
    path(
        "<int:id>",
        ProductViewSet.as_view(
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
        ProductViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
        name='list-create',
    ),
]
