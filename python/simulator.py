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

import argparse
from mdot_rl_interface import interface as mrl
from mdot_rl_interface import datatypes
from datetime import datetime

server = 'http://localhost:85/api/'
service_id = '1b26f00e-81ca-4aba-8c3c-d094ed8bfce2'
service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

parser = argparse.ArgumentParser(description='Generate RL test data')
parser.add_argument('--server', default='http://localhost:85/api')
parser.add_argument('--service_id', help='UUID')

# TODO: Remove the default once implemented on the server
parser.add_argument('--service_token', help='UUID',
                    default='e6e74d36-a3e4-4631-b077-4fdd703636f2')
args = parser.parse_args()


# UPLOAD
def upload(row: dict):
    try:
        uploadres = session.upload(row)  # Server side and raises exceptions for ERRORS
    except Exception as e:
        print(f'Something bad {e}')
        pass


# UPDATE
def update(row: dict):
    try:
        update_result = session.update(row)
        print(update_result)
    except:  # SessionError as se:
        pass


# DECISION
def decision(row: dict):
    try:
        decision_result = session.decision(row)
        print(decision_result)
    except:  # SessionError as se:
        pass


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
            row[columns[3]] = int(data[3])  # decision
            row[columns[4]] = data[4]  # proximal_outcome_timestamp
            row[columns[5]] = int(data[5])  # proximal_outcome
            values = []
            for idx in range(6, len(data)):
                val = {}
                # val[columns[idx]] = data[idx]
                val['name'] = columns[idx]
                val['value'] = (data[idx])  # TODO FIXME - hack to make the demo work
                # valdp = datatypes.DataPoint.from_dict(val)
                values.append(val)
            row['values'] = values

            rowdp = datatypes.DataVector.from_dict(row)
            # print(f'XXXXXX {row} \n {rowdp}')
            event = (timestamp, 'upload', rowdp)
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


if __name__ == '__main__':

    server = args.server
    service_id = args.service_id
    algo_id = 'c15e837c-adf1-461c-af11-2b2877cc62bb'
    service_token = args.service_token

    session = mrl.Interface(server, algo_id, service_token)

    process_upload()
    #process_update()
    #process_decision()
    allevents.sort(key=lambda x: x[0])
    print(f'All events = {len(allevents)}')

    # simulation
    count = 0
    for event in allevents:
        if event[1] == 'upload':
            data = event[2]
            upload(data)
        elif event[1] == 'update':
            update(event[2])
        else:
            decision(event[2])

        count += 1
        if count == 1: break
