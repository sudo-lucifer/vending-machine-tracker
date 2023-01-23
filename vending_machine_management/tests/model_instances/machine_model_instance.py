from model_bakery.recipe import Recipe

from vending_machine_management.models.machine import Machine

machine_instance: Recipe = Recipe(Machine)
