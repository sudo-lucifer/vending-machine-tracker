import json
from typing import Dict, List

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from vending_machine_management.serializers.machine_serializer import MachineSerializer
from vending_machine_management.tests.model_instances.machine_model_instance import machine_instance


class TestListMachineView(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.machine_1 = machine_instance.make()
        cls.machine_2 = machine_instance.make()
        cls.url = reverse("vending_machine:list-create")

    def test_list_machine(self):
        response = self.client.get(self.url)

        expected_result: List[Dict[str, str]] = [
            MachineSerializer(self.machine_1).data,
            MachineSerializer(self.machine_2).data,
        ]
        response_data: List[Dict[str, str]] = json.loads(json.dumps(response.data))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response_data, expected_result)
