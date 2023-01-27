from dataclasses import dataclass

from dataclasses_json import dataclass_json

from vending_machine_management.models.machine import Machine


@dataclass_json
@dataclass
class MachineDataclass:
    """Dataclass for machine model."""

    id: int
    name: str
    location: str

    @classmethod
    def from_model(cls, machine_instance: Machine) -> 'MachineDataclass':
        """Categorize raw machine model to dataclass.

        :param machine_instance: query instance from machine model
        :return: dataclass representation of machine query instance
        """
        return cls(id=machine_instance.id, name=machine_instance.name, location=machine_instance.location)
