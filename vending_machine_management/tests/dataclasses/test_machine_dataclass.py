from django.test import TestCase

from vending_machine_management.dataclasses.machine_dataclass import MachineDataclass
from vending_machine_management.models.machine import Machine
from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestMachineDataclass(TestCase):
    """Test class for machine dataclass with machine query instance."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock machine instance in database.

        :return: None
        """
        cls.machine: Machine = machine_instance.make()

    def test_machine_dataclass_from_model(self) -> None:
        """Test from_model() to return the dataclass version of machine query instance."""
        expected_result: MachineDataclass = MachineSerializer(self.machine).data
        dataclass_result_from_model: MachineDataclass = MachineDataclass.from_model(
            machine_instance=self.machine
        ).to_dict()
        self.assertEqual(expected_result, dataclass_result_from_model)
