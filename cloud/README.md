# Cloud details go here


## Initialize the environment
Create a python virtual environment for `python3.7` or greater.  This is one option, or you can use IntelliJ's method.  
Once created, make sure that IntelliJ is using this environment.
```bash
virtualenv -p python3.8 RL
source RL/bin/activate
```

Install all python3 requirements from `requirements.txt` or use InteliJ to install the requirements when prompted.
```bash
pip3 install -r requirements.txt
```

Initialize the testing database `mDOT_RL_development.db`
```bash
python3 manage.py db init
python3 manage.py db migrate -m 'New data'
python3 manage.py db upgrade
```

Configure IntelliJ run configuration.

1. Script path: (e.g. `/Users/hnat/mDOT/software/reinforcement-learning/cloud/manage.py`)
2. Parameters `run`