#  Copyright (c) 2022. University of Memphis, mDOT Center
# 
#  Redistribution and use in source and binary forms, with or without modification, are permitted
#  provided that the following conditions are met:
# 
#  1. Redistributions of source code must retain the above copyright notice, this list of conditions
#  and the following disclaimer.
# 
#  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions
#  and the following disclaimer in the documentation and/or other materials provided with the distribution.
# 
#  3. Neither the name of the copyright holder nor the names of its contributors may be used to
#  endorse or promote products derived from this software without specific prior written permission.
# 
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
#  ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
#  WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
#  IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
#  INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
#  NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
#  WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY
#  OF SUCH DAMAGE.
# 


from dataclasses import dataclass
from typing import Any


# TODO: What are the other members of this class?
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


# TODO: What are the other members of this class?
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
