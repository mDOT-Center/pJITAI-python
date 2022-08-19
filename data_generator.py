import argparse
from datetime import datetime, timedelta
from pathlib import Path
from pprint import pprint
import numpy as np
import random

parser = argparse.ArgumentParser(description='Generate RL test data')
parser.add_argument('--path', default='.')
parser.add_argument('--start_date', help='Start date (YYYYMMDD)')
parser.add_argument('--end_date', help='End date (YYYYMMDD)')
parser.add_argument('--user', help='User base name', default='user')
parser.add_argument('--user_count', help='Number of users',
                    type=int, default=1)
args = parser.parse_args()


user_parameters = {}


def gaussian(mean, std):
    return np.random.normal(mean, std)


def random_30_min_step_count():
    temp = np.random.uniform(-0.69, 6.9)
    return int(np.exp(temp))


def time_8601(time=datetime.now()) -> str:
    return time.astimezone().isoformat()


def _uploadGenerator(path, user_list, start_date, end_date):
    prompt_times = [(8, 30), (12, 00), (15, 00), (17, 30), (20, 00)]
    with open(Path(path).joinpath('upload.csv'), 'w') as output_file:
        output_file.write(
            'user_id,timestamp,decision_timestamp,decision,proximal_outcome_timestamp,proximal_outcome,step_count\n')
        current_date = start_date
        while current_date < end_date:
            for user_id in user_list:
                for (h, m) in prompt_times:
                    step_count = random_30_min_step_count()
                    decision_time = datetime(year=current_date.year,
                                             month=current_date.month,
                                             day=current_date.day,
                                             hour=h,
                                             minute=m,
                                             second=0)
                    decision = 0 if random.random() < 0.4 else 1

                    proximal_outcome_time = decision_time + \
                        timedelta(minutes=30)
                    proximal_outcome = int(np.exp(np.log(
                        step_count) * user_parameters[user_id][0] + user_parameters[user_id][1] + decision * user_parameters[user_id][2]))
                    output_file.write(
                        f'{user_id},{time_8601(proximal_outcome_time + timedelta(minutes=5))},{time_8601(decision_time)},{decision},{time_8601(proximal_outcome_time)},{proximal_outcome},{step_count}\n')
            current_date += timedelta(days=1)
    pass


def _decisionGenerator(path, user_list, start_date, end_date):
    prompt_times = [(8, 30), (12, 00), (15, 00), (17, 30), (20, 00)]
    with open(Path(path).joinpath('decision.csv'), 'w') as output_file:
        output_file.write('user_id,timestamp,step_count\n')
        current_date = start_date
        while current_date < end_date:
            for user_id in user_list:
                for (h, m) in prompt_times:
                    decision_time = datetime(year=current_date.year,
                                             month=current_date.month,
                                             day=current_date.day,
                                             hour=h,
                                             minute=m,
                                             second=0)
                    step_count = random_30_min_step_count()
                    output_file.write(
                        f'{user_id},{time_8601(decision_time)},{step_count}\n')
            current_date += timedelta(days=1)


def _updateGenerator(path, user_list, start_date, end_date):
    with open(Path(path).joinpath('update.csv'), 'w') as output_file:
        output_file.write('user_id,timestamp\n')
        current_date = start_date
        while current_date < end_date:
            for user_id in user_list:
                output_file.write(f'{user_id},{time_8601(current_date)}\n')
            current_date += timedelta(days=1)


if __name__ == '__main__':
    start_date = datetime.strptime(args.start_date, '%Y%m%d')
    end_date = datetime.strptime(args.end_date, '%Y%m%d')
    user = args.user

    user_list = [f'{user}_{i}' for i in range(args.user_count)]
    for user in user_list:
        user_parameters[user] = (gaussian(0.41, 0.03), gaussian(
            1.53, 0.13), gaussian(0.13, 0.07))
    pprint(user_parameters)
    _updateGenerator(args.path, user_list, start_date, end_date)
    _decisionGenerator(args.path, user_list, start_date, end_date)
    _uploadGenerator(args.path, user_list, start_date, end_date)
