from rest_framework.serializers import ModelSerializer

from vending_machine_management.models.machine import Machine


class MachineSerializer(ModelSerializer):
    class Meta:
        model = Machine
        fields = "__all__"
