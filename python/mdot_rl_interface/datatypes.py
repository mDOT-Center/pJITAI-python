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
from pprint import pprint

from .util import time_8601

@dataclass(frozen=True)
class DataPoint:
    name: str
    value: Any

    @classmethod
    def from_dict(cls, input_dict):
        d = cls(
            name=input_dict["name"],
            value=input_dict["value"], )
        return d

    def __str__(self):
        return f"{self.name}: {self.value}"

    def as_dict(self):
        return {
            "name": self.name,
            "value": self.value,
        }



@dataclass(frozen=True)
class RealmResponse:
    user_id: str
    timestamp: str = time_8601()
    status_code: str = ""
    status_message: str = ""
    selection: str = None
    
    def as_dict(self):
        result = {
            "timestamp": self.timestamp,
            "user_id": self.user_id,
            "status_code": self.status_code,
            "status_message": self.status_message
        }
        if self.selection is not None:
            result['selection'] = self.selection
        
        return 
    @classmethod
    def from_dict(cls, input_dict):
        if "selection" not in input_dict:
            input_dict["selection"] = None
        if "timestamp" not in input_dict: # TODO: is this correct?
            input_dict["timestamp"] = time_8601()
        if "user_id" not in input_dict: # TODO: is this correct?
            input_dict["user_id"] = "all"
            
        d = RealmResponse(
            timestamp=input_dict["timestamp"],
            user_id=input_dict["user_id"],
            status_code=input_dict["status_code"],
            status_message=input_dict["status_message"],
            selection=input_dict['selection'],
        )

        return d

@dataclass(frozen=True)
class DataVector:
    values: list[DataPoint]
    user_id: str
    timestamp: str = time_8601()
    status_code: str = ""
    status_message: str = ""
    decision_timestamp: str = ""
    decision: int = 0
    proximal_outcome: int = 0
    proximal_outcome_timestamp: str = ""

    def as_dict(self):
        return {
            "timestamp": self.timestamp,
            "user_id": self.user_id,
            "decision_timestamp": self.decision_timestamp,
            "decision": self.decision,
            "proximal_outcome": self.proximal_outcome,
            "proximal_outcome_timestamp": self.proximal_outcome_timestamp,
            "values": [v.as_dict() for v in self.values],

        }

    def add_value(self, data_point: dict):
        self.values.append(DataPoint.from_dict(data_point))

    @classmethod
    def from_dict(cls, input_dict):
        if "status_code" not in input_dict:
            input_dict["status_code"] = ""
        if "status_message" not in input_dict:
            input_dict["status_message"] = ""

        # pprint(input_dict)
        # decision_timestamp,decision,proximal_outcome_timestamp,proximal_outcome
        d = DataVector(
            timestamp=input_dict["timestamp"],
            user_id=input_dict["user_id"],
            values=[DataPoint.from_dict(v) for v in input_dict["values"]],
            status_code=input_dict["status_code"],
            status_message=input_dict["status_message"],
            decision_timestamp=input_dict['decision_timestamp'],
            decision=input_dict['decision'],
            proximal_outcome=input_dict['proximal_outcome'],
            proximal_outcome_timestamp=input_dict['proximal_outcome_timestamp']
        )

        return d
