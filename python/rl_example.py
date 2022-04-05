# %%
from mdot_reinforcement_learning import reinforcement_learning as mrl


server = 'https://localhost:8080/api/v1/rl/'
service_id = '6d93aff2-c619-4695-a5ab-b00ad60759f3'
service_token = 'e6e74d36-a3e4-4631-b077-4fdd703636f2'

session = mrl.reinforcement_learning(server, service_id, service_token)


# %%
