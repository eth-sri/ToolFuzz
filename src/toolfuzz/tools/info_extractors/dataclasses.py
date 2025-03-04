from dataclasses import dataclass
from typing import List, Any


@dataclass
class ArgumentType:
    name: str
    sub_types: List[Any] = None
    has_subtype: bool = False

    def __str__(self):
        return "{'type': '" + self.name + ",'has_subtype': '" + str(self.has_subtype) + "'" + ",'sub_types': " + str(
            self.sub_types) + "}"


@dataclass
class ToolArgument:
    name: str
    type: ArgumentType
    description: str
    default: Any
    has_default: bool = False

    def __str__(self):
        # return format like: {'endpoint': {'description': None, 'type': 'str'}, 'parameters': {'description': None, 'type': 'dict'}}
        description = self.description if self.description else 'None'
        return "{'" + self.name + "': {'description': '" + description + "', 'type': '" + self.type.name + "'}}"

    def __repr__(self):
        description = self.description if self.description else 'None'
        return ("{'" + self.name +
                "': {'description': '" + description + "', 'type': '" + str(
                    self.type) + "', 'default': " + str(self.default) + ", 'has_default': " + str(
                    self.has_default) + "}}")
