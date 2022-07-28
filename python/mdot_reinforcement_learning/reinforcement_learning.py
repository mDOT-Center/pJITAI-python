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

import requests
from python.mdot_reinforcement_learning.util import url_builder

# Main class
from python.mdot_reinforcement_learning.codes import StatusCode
from python.mdot_reinforcement_learning.datatypes import RLFeatureVector
from python.mdot_reinforcement_learning.exceptions import RLValidationError


class reinforcement_learning:
    model = {}
    service_url = ''
    service_token = ''

    def __init__(self, server: str, service_id: str, service_token: str):
        """Initialize the mDOT_RL class and connect to the mDOT Reinforcement Learning API.

        Args:
            server (_str_): Server URL.  (e.g. https://api.mdot.md2k.org/v1)
            service_id (_str_): Reinformcement Learning Service ID (e.g. 1387e0b3-0f18-4526-8a70-c5bad1e050f0). This can be found in the mDOT Reinforcement Learning Dashboard for a configured RL service.
            service_token (_str_): Security token for this service (e.g. bed66390-eba4-4a16-9b11-01accda7060d). This can be found in the mDOT Reinforcement Learning Dashboard for a configured RL service.
        """

        self.service_url = url_builder(server, service_id)
        self.service_token = service_token

        r = requests.post(self.service_url, headers={'RLToken': self.service_token}, json={},)
        r.raise_for_status()  # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            self.model = r.json()  # Save the RL model returned from the server

    def get_rl_service_info(self) -> dict:
        """Get the service info for the RL service.

        Returns:
            _dict_: Service info.
        """
        pass
    def get_algorithm_info(self, uuid: str) -> dict:
        """Get the service info for the RL service.

        Returns:
            _dict_: Service info.
        """
        r = requests.post(self.service_url, headers={'RLToken': self.service_token},
                          json={"data": {}})
        r.raise_for_status()  # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            result = r.json()
            print(f'Result is {result}')
            return result
        pass

    def upload(self, data: dict) -> dict:
        """Batch upload data for the RL model.

        Args:
            data (_dict_): Data to update the RL model.

        Returns:
            _dict_: Updated RL model.
        """

        # Validate the data
        # valid = validate_parameters(self.model, data)
        valid = True
        if valid:
            # Send to the server
            r = requests.post(self.service_url + '/upload', headers={'RLToken': self.service_token},
                              json=data)
            r.raise_for_status()  # Raise an exception if the request fails for any reason
            if r.status_code == requests.codes.ok:
                result = r.json()
                #print(f'upload result {result}')
                return result
        else:
            raise Exception("Data is not valid")

    def batch_upload(self, data: dict) -> dict:
        """Batch upload data for the RL model.

        Args:
            data (_dict_): Data to update the RL model.

        Returns:
            _dict_: Updated RL model.
        """

        # Validate the data
        # valid = validate_parameters(self.model, data)
        valid = True
        if valid:
            # Send to the server
            r = requests.post(self.service_url + '/upload', headers={'RLToken': self.service_token},
                              json={"data": data})
            r.raise_for_status()  # Raise an exception if the request fails for any reason
            if r.status_code == requests.codes.ok:
                result = r.json()
                return result
        else:
            raise Exception("Data is not valid")

    def decision(self, data: RLFeatureVector) -> RLFeatureVector:
        """Make a decision based on the RL model.

        Args:
            data (_dict_): Data to make a decision.

        Returns:
            _dict_: Decision.
        """

        # Validate the data
        # valid = validate_parameters(self.model, data)
        valid = True
        if valid:
            # Send to the server
            r = requests.post(self.service_url + '/decision',
                              headers={'RLToken': self.service_token},
                              json=data)
            r.raise_for_status()
            if r.status_code == requests.codes.ok:
                result = RLFeatureVector.from_dict(r.json())  # Convert back to RLFeatureVector
                return result
        else:
            raise Exception("Data is not valid")


    def update(self, data: RLFeatureVector) -> RLFeatureVector:
        """Make a decision based on the RL model.

        Args:
            data (_dict_): Data to make a decision.

        Returns:
            _dict_: Decision.
        """

        # Validate the data
        # valid = validate_parameters(self.model, data)
        valid = True
        if valid:
            # Send to the server
            r = requests.post(self.service_url + '/update',
                              headers={'RLToken': self.service_token},
                              json=data)
            r.raise_for_status()
            if r.status_code == requests.codes.ok:
                result = RLFeatureVector.from_dict(r.json())  # Convert back to RLFeatureVector
                return result
        else:
            raise Exception("Data is not valid")

    def validate_data(self, data: RLFeatureVector) -> RLFeatureVector:
        """
        Send the data to the server for validation and return the validated data with the additional validation fields.

        :param data:
        :return:
        """

        # Send to the server
        r = requests.post(self.service_url + '/validate_data',
                          headers={'RLToken': self.service_token},
                          json=data.as_dict())

        r.raise_for_status()  # Raise an exception if the request fails for any reason

        if r.status_code == requests.codes.ok:
            result = RLFeatureVector.from_dict(r.json())  # Convert back to RLFeatureVector
            for feature in result.values:
                if feature.status_code == StatusCode.ERROR:
                    # TODO: How to handle multiple simultaneous validation errors?
                    raise RLValidationError(f'{feature.name}: {feature.status_message}')
            return result
'''
Add for batch updates
Add for decisions
'''