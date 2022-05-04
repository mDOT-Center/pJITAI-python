# Helper methods to suppor the reinforcement learning library

def validate_parameters(model, data) -> bool:
    # Pass in the model JSON and data.  This should ensure that the data is valid and throw an exception if it is not.
    valid = True

    if data == valid:
        return True
    else:
        raise Exception("Invalid data")  # Needs more detail here


def url_builder(server, service_id) -> str:
    # Build the URL for the API call
    url = server + "/" + service_id
    return url
