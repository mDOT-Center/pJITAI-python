import unittest
from pprint import pprint

from mdot_reinforcement_learning.util import url_builder, time_8601
import responses
import random

from mdot_reinforcement_learning import reinforcement_learning as mrl
from python.mdot_reinforcement_learning.datatypes import RLPoint


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
        validate_data_input = []
        for i in range(2):
            validate_data_input.append(RLPoint(
                timestamp=time_8601(),
                value=random.random(),
                name=f'feature_{i}',
            ))

        validate_data_output = [RLPoint(name=x.name, value=x.value, timestamp=x.timestamp, status_code='SUCCESS',
                                        status_message='DATA_VALIDATED') for x in validate_data_input]

        server_response = {
            'timestamp': '2022-05-05T13:47:51.557803-05:00',
            'values': [
                {
                    'name': 'feature_0',
                    'value': 1.234,
                    'timestamp': '2022-05-05T13:47:51.557803-05:00',
                    'status_code': 'SUCCESS',
                    'status_message': 'DATA_VALIDATED',
                },
                {
                    'name': 'feature_1',
                    'value': 86,
                    'timestamp': '2022-05-05T13:47:51.557803-05:00',
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
        pprint(validate_result)
        self.assertEqual(validate_result, validate_data_output)


if __name__ == '__main__':
    unittest.main()
