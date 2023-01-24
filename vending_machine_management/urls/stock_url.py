from django.urls import path

from vending_machine_management.views.stock_view_set.stock_create_view import StockCreateView
from vending_machine_management.views.stock_view_set.stock_delete_view import StockDeleteView
from vending_machine_management.views.stock_view_set.stock_detail_view import StockDetailView
from vending_machine_management.views.stock_view_set.stock_edit_view import StockEditView
from vending_machine_management.views.stock_view_set.stock_list_view import StockListView

stock_urls = [
    path("list", StockListView.as_view(), name="list"),
    path("detail/<int:id>", StockDetailView.as_view(), name='detail'),
    path("create", StockCreateView.as_view(), name='create'),
    path("delete/<int:id>", StockDeleteView.as_view(), name='delete'),
    path("edit/<int:id>", StockEditView.as_view(), name='edit'),
]
