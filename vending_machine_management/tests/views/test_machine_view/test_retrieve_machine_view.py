import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.dataclasses.machine_dataclass import MachineDataclass
from vending_machine_management.models.machine import Machine
from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestRetrieveMachineView(APITestCase):
    """Test class for getting one machine detail from database."""

    @classmethod
    def setUpTestData(cls) -> None:
        """Test hook to mock machine instance in database.

        :return: None
        """
        cls.machine_1: Machine = machine_instance.make()

    def test_retrieve_single_machine(self) -> None:
        """Test getting existing machine detail."""
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_1.id})
        response = self.client.get(url)

        expected_result: MachineDataclass = MachineSerializer(self.machine_1).data
        response_data: MachineDataclass = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, expected_result)

    def test_retrieve_single_machine_not_found(self) -> None:
        """Test getting non-existing machine detail."""
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_1.id + 1})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
