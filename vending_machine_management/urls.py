"""vending_machine_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import include, path

from vending_machine_management.views.machine_view import MachineViewSet
from vending_machine_management.views.product_view import ProductViewSet
from vending_machine_management.views.stock_view_set.stock_create_view import StockCreateView
from vending_machine_management.views.stock_view_set.stock_delete_view import StockDeleteView
from vending_machine_management.views.stock_view_set.stock_detail_view import StockDetailView
from vending_machine_management.views.stock_view_set.stock_edit_view import StockEditView
from vending_machine_management.views.stock_view_set.stock_list_view import StockListView

base_url_vending_machine = "machine"
base_url_stock = "stock"
base_url_product = "product"

stock = [
    path("list", StockListView.as_view()),
    path("detail/<int:id>", StockDetailView.as_view()),
    path("create", StockCreateView.as_view()),
    path("delete/<int:id>", StockDeleteView.as_view()),
    path("edit/<int:id>", StockEditView.as_view()),
]

machine = [
    path(
        "<int:id>",
        MachineViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy',
            }
        ),
    ),
    path(
        "",
        MachineViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
    ),
]

product = [
    path(
        "<int:id>",
        ProductViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy',
            }
        ),
    ),
    path(
        "",
        ProductViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
    ),
]


urlpatterns = [
    path(f"{base_url_stock}/", include((stock, "stock"), namespace="stock")),
    path(f"{base_url_vending_machine}/", include((machine, "vending_machine"), namespace="vending_machine")),
    path(f"{base_url_product}/", include((product, "product"), namespace="product")),
]
