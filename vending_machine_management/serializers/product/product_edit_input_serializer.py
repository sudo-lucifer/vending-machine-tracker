from rest_framework_dataclasses.serializers import DataclassSerializer

from vending_machine_management.dataclasses.product.product_edit_dataclass import ProductEditDataclass


class ProductEditInputSerializer(DataclassSerializer):
    class Meta:
        dataclass = ProductEditDataclass
        fields = "__all__"
