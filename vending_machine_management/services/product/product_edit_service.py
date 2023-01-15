from django.db import transaction

from vending_machine_management.dataclasses.product.product_edit_dataclass import ProductEditDataclass
from vending_machine_management.models.product import Product


class ProductEditService:
    @classmethod
    @transaction.atomic
    def edit_product(cls, product_id: int, changed_data: ProductEditDataclass):
        product = Product.objects.select_for_update().filter(id=product_id)
        if len(product) == 0:
            return None
        product.update(name=changed_data.name, price=changed_data.price)
        return Product.objects.get(id=product_id)
