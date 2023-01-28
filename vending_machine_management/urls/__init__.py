"""App vending_machine_backend URL Configuration.

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

from vending_machine_management.urls.machine_url import machine_urls
from vending_machine_management.urls.product_url import product_urls
from vending_machine_management.urls.stock_url import stock_urls

base_url_vending_machine = "machine"
base_url_stock = "stock"
base_url_product = "product"

urlpatterns = [
    path(f"{base_url_stock}/", include((stock_urls, "stock"), namespace="stock")),
    path(f"{base_url_vending_machine}/", include((machine_urls, "vending_machine"), namespace="vending_machine")),
    path(f"{base_url_product}/", include((product_urls, "product"), namespace="product")),
]
