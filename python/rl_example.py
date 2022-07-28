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

server = 'http://localhost:85/api/'
service_id = 'aceb56c4-59f9-4534-b8e7-f04d4ee39861'
service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

session = mrl.reinforcement_learning(server, service_id, service_token)


# UPLOAD
def upload():
    try:

        postman_data = {
            "timestamp": "2022-06-16T13: 41: 51.120903-05: 00",
            "user_id": "user_1",
            "values": [
                {
                    "timestamp": "2022-06-16T19:05:23.495427-05: 00",
                    "decision_timestamp": "2022-06-16T19:05:23.495427-05: 00",
                    "decision": 1,
                    "proximal_outcome_timestamp": "2022-06-16T19:05:23.495427-05: 00",
                    "proximal_outcome": 50,
                    "values": [
                        {
                            "name": "step_count",
                            "value": 500
                        }
                    ]
                }
            ]
        }
        algo_info = session.upload(postman_data)  # Server side and raises exceptions for ERRORS
    except:  # ValidationError as e:
        # Example: Remove invalid data entries
        pass


# UPDATE
def update():
    try:
        data = {}
        data['user_id'] = 'user_0'
        decision_result = session.update(data)
    except:  # SessionError as se:
        pass


# DECISION
def decision():
    try:
        data = {}
        data['user_id'] = 'user_0'
        decision_result = session.decision(data)
    except:  # SessionError as se:
        pass


# decision_result = session.decision(decision_data)

upload()
update()
decision()
# %%
