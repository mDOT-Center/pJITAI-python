#

import requests
import uuid

## Helper functions

def validate_parameters(model, data) -> bool:
    # Pass in the model JSON and data.  This should ensure that the data is valid and throw an exception if it is not.
    valid = True
    
    if data == valid:
        return True
    else:
        raise Exception("Invalid data") # Needs more detail here
    
    
def url_builder(server, service_id) -> str:
    # Build the URL for the API call
    url = server + "/" + service_id
    return url

def add_token(data, token) -> dict:
    # Add the token to the data
    data["token"] = token
    return data


# Main class

class reinforcement_learning:
    
    model = {}
    service_url = ''
    service_token = ''
    
    def __init__(self, server: str, service_id: str, service_token: str):
        """Initialize the mDOT_RL class and connect to the mDOT Reinforcement Learning API.

        Args:
            server (_str_): Server URL.  (e.g. https://api.mdot.org/v1/)
            service_id (_str_): Reinformcement Learning Service ID (e.g. 1387e0b3-0f18-4526-8a70-c5bad1e050f0). This can be found in the mDOT Reinforcement Learning Dashboard for a configured RL service.
            service_token (_str_): Security token for this service (e.g. bed66390-eba4-4a16-9b11-01accda7060d). This can be found in the mDOT Reinforcement Learning Dashboard for a configured RL service.
        """
        
        self.service_url = url_builder(server, service_id)
        self.service_token = service_token
        
        
        r = requests.post(self.service_url, json = add_token({}, self.service_token))
        r.raise_for_status() # Raise an exception if the request fails for any reason
        if r.status_code == requests.codes.ok:
            self.model = r.json() # Save the RL model returned from the server
        
    
    def get_rl_service_info(self) -> dict:
        """Get the service info for the RL service.

        Returns:
            _dict_: Service info.
        """
        pass
    
    def batch_update(self, data: dict) -> dict:
        """Batch update the RL model.

        Args:
            data (_dict_): Data to update the RL model.

        Returns:
            _dict_: Updated RL model.
        """
        
        # Validate the data
        valid = validate_parameters(self.model, data)
        
        
        if valid:
            # Send to the server
            r = requests.post(self.service_url, json =  add_token({"data": data}, self.service_token))
            r.raise_for_status() # Raise an exception if the request fails for any reason
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
        valid = validate_parameters(self.model, data)
        
        
        if valid:
            # Send to the server
            r = requests.post(self.service_url, json =  add_token({"data": data}, self.service_token))
            r.raise_for_status()
            if r.status_code == requests.codes.ok:
                result = r.json()
                return result
        else:
            raise Exception("Data is not valid")
        