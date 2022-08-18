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

from typing import Any
import requests

from .datatypes import DataVector, DecisionResponse, UpdateResponse, UploadResponse
from .util import url_builder
from requests.exceptions import HTTPError


class Client:
    """Primary pJITAI client.
    
    Implements:
    - Upload
    - Update
    - Decision
    
    """
    service_url = ''
    service_token = ''
    model: dict[Any, Any] = {}

    def __init__(self, server: str, service_id: str, service_token: str):
        """Initialization method for the client

        Args:
            server (str): URL for the path to the server api (e.g. https://pJITAI.md2k.org/api)
            service_id (str): UUID designation for the specific algorithm instance
            service_token (str): UUID security token for the algorithm instance

        Raises:
            Exception: General purpose exception with a description of any error.
        """
        self.service_url = url_builder(server, service_id)
        self.service_token = service_token
        try:
            r = requests.post(self.service_url, headers={
                              'pJITAI_token': self.service_token},
                              json={})
            r.raise_for_status()
            self.model = r.json()  # Save the pJITAI model returned from the server

        except HTTPError as exc:
            code = exc.response.status_code

            if code in [400]:
                raise Exception(f'{r.status_code} {r.json()}')

            raise Exception(f'{code} {r.json()}')

    def get_algorithm_info(self) -> dict:
        """Algorithm instance details from the server.

        Returns:
            dict: A diction containing all the details of the algorithm defination
        """
        return self.model

    def upload(self, data: DataVector) -> UploadResponse:
        """Upload data for storage in the pJITAI server.

        Args:
            data (DataVector): A DataVector containing all the necessary information for a single uploaded point.  This is currently limited to a single entry per upload.

        Raises:
            Exception: General purpose exception with a description of any error.

        Returns:
            UploadResponse: Response details from the server
        """
        try:
            r = requests.post(self.service_url + '/upload',
                              headers={'pJITAI_token': self.service_token},
                              json=data.as_dict())
            r.raise_for_status()  # Raise an exception if the request fails for any reason

            result = UploadResponse.from_dict(r.json())
            return result

        except HTTPError as exc:
            code = exc.response.status_code

            if code in [400]:
                raise Exception(f'{r.status_code} {r.json()}')

            raise Exception(f'{code} {r.json()}')

    def update(self) -> UpdateResponse:
        """Initiate this algorithm's update operation on the server.
        
        This is an asynchronous operation and will return once it launches.
        There is currently no mechanism to check for the completion of this operation.

        Raises:
            Exception: General purpose exception with a description of any error.

        Returns:
            UpdateResponse: Response details from the server.
        """
        try:
            r = requests.post(self.service_url + '/update',
                              headers={'pJITAI_token': self.service_token},
                              json={})
            r.raise_for_status()
            result = UpdateResponse.from_dict(r.json())
            return result

        except HTTPError as exc:
            code = exc.response.status_code

            if code in [400]:
                raise Exception(f'{r.status_code} {r.json()}')

            raise Exception(f'{code} {r.json()}')

    def decision(self, covariates: DataVector) -> DecisionResponse:
        """_summary_

        Args:
            features (DataVector): A DataVector representing all the covariates defined by the algorithm instance.

        Raises:
            Exception: General purpose exception with a description of any error.

        Returns:
            DecisionResponse: Response details from the server
        """
        try:
            r = requests.post(self.service_url + '/decision',
                              headers={'pJITAI_token': self.service_token},
                              json=covariates)
            r.raise_for_status()
            result = DecisionResponse.from_dict(r.json())
            return result

        except HTTPError as exc:
            code = exc.response.status_code

            if code in [400]:
                raise Exception(f'{r.status_code} {r.json()}')

            raise Exception(f'{code} {r.json()}')
