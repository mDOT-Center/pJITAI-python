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


import unittest
from pprint import pprint

from mdot_reinforcement_learning.util import url_builder, time_8601
import responses
import random

from mdot_reinforcement_learning import reinforcement_learning as mrl
from python.mdot_reinforcement_learning.datatypes import RLPoint, RLFeatureVector


class TestRLMethods(unittest.TestCase):

    @responses.activate
    def setUp(self):
        self.server = 'https://localhost:8080/api/v1/rl'
        self.service_id = '6d93aff2-c619-4695-a5ab-b00ad60759f3'
        self.service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

        responses.add(responses.POST, url_builder(self.server, self.service_id), json={'foo': 'bar'}, status=200)
        self.session = mrl.reinforcement_learning(
            self.server, self.service_id, self.service_token)

    def test_setup(self):
        self.assertEqual(self.session.model, {'foo': 'bar'})

    @responses.activate
    def test_batch_upload(self):
        batch_data = {
            'data': [
                [1, 2, 3, 4, 5],
                [5, 4, 3, 2, 1],
                [0, 0, 0, 1, 0],
                [4, 3, 2, 1, 0],
            ]
        }

        responses.add(responses.POST, url_builder(self.server, self.service_id) + '/batch_upload',
                      json={'batch_upload': 'bar'}, status=200)

        batch_upload_result = self.session.batch_upload(batch_data)
        self.assertEqual(batch_upload_result, {'batch_upload': 'bar'})

    @responses.activate
    def test_data_validation_clean(self):
        validate_data_input = RLFeatureVector(
            timestamp=time_8601(),
            user_id='user_1',
            values=[RLPoint(
                timestamp=time_8601(),
                value=random.random(),
                name=f'feature_{i}',
            ) for i in range(2)],
        )

        validate_data_output = RLFeatureVector(
            timestamp=validate_data_input.timestamp,
            user_id=validate_data_input.user_id,
            values=[RLPoint(name=x.name, value=x.value, timestamp=x.timestamp, status_code='SUCCESS',
                            status_message='DATA_VALIDATED') for x in validate_data_input.values]
        )

        server_response = {
            'timestamp': validate_data_input.timestamp,
            'user_id': validate_data_input.user_id,
            'values': [
                {
                    'name': validate_data_input.values[0].name,
                    'value': validate_data_input.values[0].value,
                    'timestamp': validate_data_input.values[0].timestamp,
                    'status_code': 'SUCCESS',
                    'status_message': 'DATA_VALIDATED',
                },
                {
                    'name': validate_data_input.values[1].name,
                    'value': validate_data_input.values[1].value,
                    'timestamp': validate_data_input.values[1].timestamp,
                    'status_code': 'SUCCESS',
                    'status_message': 'DATA_VALIDATED',
                },
            ]
        }

        responses.add(responses.POST,
                      url_builder(self.server, self.service_id) + '/validate_data',
                      json=server_response,
                      status=200)

        validate_result = self.session.validate_data(validate_data_input)
        self.assertEqual(validate_result, validate_data_output)


if __name__ == '__main__':
    unittest.main()
