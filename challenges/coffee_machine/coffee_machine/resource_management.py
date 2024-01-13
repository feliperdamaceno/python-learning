from copy import deepcopy
from dataclasses import dataclass, field


@dataclass
class Resource:
    name: str
    quantity: int
    unit: int


@dataclass
class ResourceManagement:
    _initial_resources: list[Resource] = field(
        init=False, repr=False, default_factory=list
    )
    _resources: list[Resource] = field(init=False, repr=False, default_factory=list)

    @property
    def resources(self) -> list[Resource]:
        return self._resources

    @resources.setter
    def resources(self) -> None:
        raise ValueError("This operation is not available.")

    def create_resources(self, resources: list[Resource]) -> None:
        self._initial_resources = resources
        self._resources = deepcopy(self._initial_resources)

    def get_resource(self, resource_name: str) -> Resource:
        resource = [
            resource for resource in self._resources if resource.name == resource_name
        ]

        if not resource:
            raise ValueError(f"The resource {resource_name} has not been found")

        return resource[0]

    def use_resource(self, resource_name: str, quantity: int) -> None:
        resource = self.get_resource(resource_name)

        if quantity > resource.quantity:
            resource.quantity = 0
            return

        resource.quantity -= quantity

    def reset_resources(self) -> None:
        self._resources = deepcopy(self._initial_resources)
