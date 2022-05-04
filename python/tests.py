import unittest
from mdot_reinforcement_learning.util import url_builder
import responses


from mdot_reinforcement_learning import reinforcement_learning as mrl


class TestRLMethods(unittest.TestCase):

    @responses.activate
    def setUp(self):
        self.server = 'https://localhost:8080/api/v1/rl'
        self.service_id = '6d93aff2-c619-4695-a5ab-b00ad60759f3'
        self.service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

        responses.add(responses.POST, url_builder(
            self.server, self.service_id), json={'foo': 'bar'}, status=200)
        responses.add(responses.POST, url_builder(
            self.server, self.service_id) + '/batch_update', json={'batch_update': 'bar'}, status=200)
        responses.add(responses.POST, url_builder(
            self.server, self.service_id) + '/decision', json={'decision': 'bar'}, status=200)

        self.session = mrl.reinforcement_learning(
            self.server, self.service_id, self.service_token)

    def test_setup(self):
        self.assertEqual(self.session.model, {'foo': 'bar'})

    def test_batch_update(self):
       batch_data = {
           'data': [
               [1, 2, 3, 4, 5],
               [5, 4, 3, 2, 1],
               [0, 0, 0, 1, 0],
               [4, 3, 2, 1, 0],
           ]
       }
       batch_update_result = self.session.batch_upload(batch_data)
       self.assertEqual(batch_update_result, {'foo': 'bar'})

    def test_decision_data(self):
        decision_data = {
            'data': [
                [1, 2, 3, 4, 5],
            ]
        }
        decision_result = self.session.decision(decision_data)
        self.assertEqual(decision_result, {'foo': 'bar'})



if __name__ == '__main__':
    unittest.main()
