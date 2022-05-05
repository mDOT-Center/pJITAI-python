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


# %%
from mdot_reinforcement_learning import reinforcement_learning as mrl

server = 'https://localhost:8080/api/v1/rl'
service_id = '6d93aff2-c619-4695-a5ab-b00ad60759f3'
service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

session = mrl.reinforcement_learning(server, service_id, service_token)

batch_data = {
    'data': [
        [1, 2, 3, 4, 5],
        [5, 4, 3, 2, 1],
        [0, 0, 0, 1, 0],
        [4, 3, 2, 1, 0],
    ]
}

possible_codes = [
    'ERROR_INVALID_DATA_VALUE',
    'ERROR_DATA_VALUE_TOO_SMALL',
    'ERROR_DATA_VALUE_TOO_LARGE',
    'ERROR_INVALID_DATA_TYPE',

    'WARNING_MISSING_DATA',

    'SUCCESS_DATA_VALIDATED',
]

decision_data = {
    'timestamp': '2020-01-01T00:00:00Z-06:00',
    'data': [
        {
            'name': 'feature0',
            'value': 1.234,
            'timestamp': '2022-05-04T11:52:00Z-06:00',
            'status_code': 'SUCCESS',
            'status_message': 'DATA_VALIDATED',
        },
        {
            'name': 'feature1_heart_rate',
            'value': 100000000,
            'timestamp': '2022-05-03T11:52:00Z-06:00',
            'status_code': 'SUCCESS',
            'status_message': 'DATA_VALIDATED',
        },
        {
            'name': 'feature1_heart_rate',
        }
    ]
}

# Option 1

try:
    validated_data = session.validate_data(batch_data)  # Server side and raises exceptions for ERRORS
except ValidationError as e:
    # Example: Remove invalid data entries
    pass

try:
    batch_upload_result = session.batch_upload(
        validated_data)  # Server validate before saving data, Returns errors if any and the client raises and exception
except SessionError as se:
    pass

decision_result = session.decision(decision_data)

# %%
