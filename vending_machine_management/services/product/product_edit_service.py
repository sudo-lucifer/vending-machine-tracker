from django.db import transaction

from vending_machine_management.dataclasses.product.product_edit_dataclass import ProductEditDataclass
from vending_machine_management.models.product import Product


class ProductEditService:
    @classmethod
    @transaction.atomic
    def edit_product(cls, product_id: int, changed_data: ProductEditDataclass):
        """
        :param product_id: id of product to be updated
        :param changed_data: serialized data from user
        :return: query set of product given by ID or None if does not exist

        Remark: using filter to make sure API does not crash when product does not exist
        """
        product = Product.objects.select_for_update().filter(id=product_id)
        if len(product) == 0:
            return None
        product.update(name=changed_data.name, price=changed_data.price)
        return Product.objects.get(id=product_id)
