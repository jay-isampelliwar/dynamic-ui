from dataclasses import dataclass, field, asdict
from typing import List, Dict
from enum import Enum
import json


class SchemaType(str, Enum):
    FUNCTION = "function"


class PropertyType(str, Enum):
    NUMBER = "number"


@dataclass
class ParameterProperty:
    type: PropertyType

    def to_json(self):
        return {"type": self.type.value}

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)


@dataclass
class Parameters:
    type: str  # Still a string like "object"
    properties: Dict[str, ParameterProperty]
    required: List[str]
    additionalProperties: bool

    def to_json(self):
        return {
            "type": self.type,
            "properties": {k: v.to_json() for k, v in self.properties.items()},
            "required": self.required,
            "additionalProperties": self.additionalProperties,
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)


@dataclass
class Function:
    name: str
    description: str
    parameters: Parameters
    strict: bool

    def to_json(self):
        return {
            "name": self.name,
            "description": self.description,
            "parameters": self.parameters.to_json(),
            "strict": self.strict,
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)


@dataclass
class FunctionWrapper:
    type: SchemaType
    function: Function

    def to_json(self):
        return {
            "type": self.type.value,
            "function": self.function.to_json(),
        }

    def __str__(self):
        return json.dumps(self.to_json(), indent=2)