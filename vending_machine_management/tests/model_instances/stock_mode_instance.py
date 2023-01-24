from model_bakery.recipe import Recipe

from vending_machine_management.models.stock import Stock

stock_instance: Recipe = Recipe(Stock)
