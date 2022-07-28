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

from mdot_reinforcement_learning import reinforcement_learning as mrl
from datetime import datetime

server = 'http://localhost:85/api/'
service_id = 'aceb56c4-59f9-4534-b8e7-f04d4ee39861'
service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

session = mrl.reinforcement_learning(server, service_id, service_token)


# UPLOAD
def upload(row: dict):
    try:
        data = {}
        data['timestamp'] = row['timestamp']
        data['user_id'] = row['user_id']
        data['values'] = [row]
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
        uploadres = session.upload(data)  # Server side and raises exceptions for ERRORS
        #print(uploadres)
    except:  # ValidationError as e:
        # Example: Remove invalid data entries
        pass


# UPDATE
def update(row: dict):
    try:
        decision_result = session.update(row)
    except:  # SessionError as se:
        pass


# DECISION
def decision(row: dict):
    try:
        decision_result = session.decision(row)
    except:  # SessionError as se:
        pass


# decision_result = session.decision(decision_data)
allevents = []


def process_upload():
    f = open('upload.csv')
    i = 0
    columns = None
    for l in f:
        if i == 0:
            columns = l.strip().split(',')
        else:
            data = l.strip().split(',')
            row = {}
            row[columns[0]] = data[0]  # user id
            row[columns[1]] = data[1]  # timestamp
            timestamp = datetime.fromisoformat(data[1])
            row[columns[2]] = data[2]  # decision_timestamp
            row[columns[3]] = data[3]  # decision
            row[columns[4]] = data[4]  # proximal_outcome_timestamp
            row[columns[5]] = data[5]  # proximal_outcome
            values = []
            for idx in range(6, len(data)):
                val = {}
                val[columns[idx]] = data[idx]
                values.append(val)
            row['values'] = values
            event = (timestamp, 'upload', row)
            allevents.append(event)

        i += 1
    f.close()


def process_update():
    f = open('update.csv')
    i = 0
    columns = None
    for l in f:
        if i == 0:
            columns = l.strip().split(',')
            # print(columns)
        else:
            data = l.strip().split(',')
            # print(data)
            row = {}
            row[columns[0]] = data[0]  # user id
            row[columns[1]] = data[1]  # timestamp
            timestamp = datetime.fromisoformat(data[1])

            event = (timestamp, 'update', row)
            allevents.append(event)

        i += 1

    f.close()


def process_decision():
    f = open('decision.csv')
    i = 0
    columns = None
    for l in f:
        if i == 0:
            columns = l.strip().split(',')
        else:
            data = l.strip().split(',')
            row = {}
            row[columns[0]] = data[0]  # user id
            row[columns[1]] = data[1]  # timestamp
            timestamp = datetime.fromisoformat(data[1])
            values = []
            for x in range(2, len(data)):
                val = {}
                val[columns[x]] = data[x]
                values.append(val)
            row['values'] = values

            event = (timestamp, 'decision', row)
            allevents.append(event)

        i += 1
    f.close()


process_upload()
process_update()
process_decision()
allevents.sort(key=lambda x: x[0])
print(f'All events = {len(allevents)}')

# simulation
count = 0
for event in allevents:
    #print(f'event is {event[1]}')
    #print(event)
    if event[1] == 'upload':
        upload(event[2])
    elif event[1] == 'update':
        update(event[2])
    else:
        decision(event[2])



