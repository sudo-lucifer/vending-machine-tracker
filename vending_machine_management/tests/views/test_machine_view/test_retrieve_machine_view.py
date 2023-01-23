import json
from typing import Dict

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestRetrieveMachineView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine_1 = machine_instance.make()

    def test_retrieve_single_machine(self):
        url = reverse("vending_machine:retrieve-update-destroy", kwargs={"id": self.machine_1.id})
        response = self.client.get(url)

        expected_result: Dict[str, str] = MachineSerializer(self.machine_1).data
        response_data: Dict[str, str] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, expected_result)
