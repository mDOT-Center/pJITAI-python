from dataclasses import dataclass
from typing import Any


from python.mdot_reinforcement_learning.util import time_8601


@dataclass(frozen=True)
class RLPoint:
    name: str
    value: Any
    timestamp: str = time_8601()
    status_code: str = ""
    status_message: str = ""

    @classmethod
    def from_dict(cls, input_dict):
        if "status_code" not in input_dict:
            input_dict["status_code"] = ""
        if "status_message" not in input_dict:
            input_dict["status_message"] = ""

        d = cls(
            name=input_dict["name"],
            value=input_dict["value"],
            timestamp=input_dict["timestamp"],
            status_code=input_dict["status_code"],
            status_message=input_dict["status_message"],
        )
        return d

    def __str__(self):
        return f"{self.name}: {self.value}"

    def as_dict(self):
        return {
            "name": self.name,
            "value": self.value,
            "timestamp": self.timestamp,
            "status_code": self.status_code,
            "status_message": self.status_message,
        }


@dataclass(frozen=True)
class RLFeatureVector:
    values: list[RLPoint]
    user_id: str
    timestamp: str = time_8601()

    def as_dict(self):
        return {
            "timestamp": self.timestamp,
            "user_id": self.user_id,
            "values": [v.as_dict() for v in self.values],
        }

    @classmethod
    def from_dict(cls, input_dict):
        d = RLFeatureVector(
            timestamp=input_dict["timestamp"],
            user_id=input_dict["user_id"],
            values=[RLPoint.from_dict(v) for v in input_dict["values"]],
        )

        return d
