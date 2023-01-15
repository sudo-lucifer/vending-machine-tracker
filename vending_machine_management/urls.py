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

from vending_machine_management.views.product_view import ProductViewSet

base_url_vending_machine = "vending-machine"
base_url_product = "product"

vending_machine = []


urlpatterns = [
    path(f"{base_url_vending_machine}/", include((vending_machine, "vending_machine"), namespace="vending_machine")),
    path(
        f"{base_url_product}/<int:id>",
        ProductViewSet.as_view(
            {
                'get': 'retrieve',
                'put': 'update',
                'delete': 'destroy',
            }
        ),
    ),
    path(
        f"{base_url_product}",
        ProductViewSet.as_view(
            {
                'get': 'list',
                'post': 'create',
            }
        ),
    ),
]
