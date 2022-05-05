#

import requests

from mdot_reinforcement_learning.util import url_builder, validate_parameters


# Main class

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

        r = requests.post(self.service_url, json={})
        r.raise_for_status()  # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            self.model = r.json()  # Save the RL model returned from the server

    def get_rl_service_info(self) -> dict:
        """Get the service info for the RL service.

        Returns:
            _dict_: Service info.
        """
        pass

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
            r = requests.post(self.service_url + '/batch_upload', headers={'RLToken': self.service_token}, json={"data": data})
            r.raise_for_status()  # Raise an exception if the request fails for any reason
            if r.status_code == requests.codes.ok:
                result = r.json()
                return result
        else:
            raise Exception("Data is not valid")

    def decision(self, data: dict) -> dict:
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
            r = requests.post(self.service_url + '/decision', headers={'RLToken': self.service_token},
                              json={"data": data})
            r.raise_for_status()
            if r.status_code == requests.codes.ok:
                result = r.json()
                return result
        else:
            raise Exception("Data is not valid")
