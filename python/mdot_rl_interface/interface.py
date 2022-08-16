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
from typing import Any
import requests

# Main class
from .datatypes import DataVector, RealmResponse
from .util import url_builder


class Interface:
    service_url = ''
    service_token = ''
    model: dict[Any, Any] = {}

    def __init__(self, server: str, service_id: str, service_token: str):
        self.service_url = url_builder(server, service_id)
        self.service_token = service_token
        r = requests.post(self.service_url, headers={'RLToken': self.service_token}, json={}, )
        r.raise_for_status()  # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            self.model = r.json()  # Save the RL model returned from the server

        pass

    def get_algorithm_info(self) -> dict:
        """

        :return:
        """
        return self.model

    def upload(self, data: DataVector) -> dict:
        """
        Uploads a single data vector row to the configured algorithm
        :param data: The DataVector object to be uploaded
        :return: Status of the operation
        """
        r = requests.post(self.service_url + '/upload', headers={'RLToken': self.service_token},
                          json=data.as_dict())
        #r.raise_for_status()  # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            result = r.json()
            return result
        else:
            raise Exception(f'{r.status_code} {r.json()}')

    def update(self) -> dict:
        """
        Requests the service to update
        :return: Status of the operation
        """
        r = requests.post(self.service_url + '/update',
                          headers={'RLToken': self.service_token},
                          json={})
        r.raise_for_status()
        if r.status_code == requests.codes.ok:
            result = RealmResponse.from_dict(r.json())
            return result
        pass

    def decision(self, features: DataVector) -> dict:
        """
        Request the service for a decision action
        :param features:
        :return: Status of the operation
        """
        r = requests.post(self.service_url + '/decision',
                          headers={'RLToken': self.service_token},
                          json=features)
        r.raise_for_status()
        if r.status_code == requests.codes.ok:
            result = RealmResponse.from_dict(r.json())
            return result
        pass
