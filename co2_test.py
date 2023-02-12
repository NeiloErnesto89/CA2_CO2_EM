import requests  
from env import API_KEY 

"""

26/01/23: (Neil) this is just an early tester to play around with the apis
for CA2 (contem_software)
idea: https://www.geodose.com/2020/08/create-flight-tracking-apps-using-python-open-data.html
"""

import requests
import json

params = {
  'api_key': API_KEY, # apikey
  'params1': 'value1'
}
method = 'flights'
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method, params) #timeout=0.5, stream=True
api_response = api_result.json()


print(json.dumps(api_response, indent=4, sort_keys=True))


# define class
# class Airplane:
    
#     # python init/constructor with some basic params  
#     def __init__(self, name, fleet_size, emission_levels):
#       self.name = name
#       self.fleet_size = fleet_size
#       self.emission_levels = emission_levels
      
""" 
At any given moment, what are the estimated total global CO2 emissions
of all of the scheduled live flights currently in the air? 
Consider only those flights with specified departure and destination airports. 
"""

# def calculate_live_flights():
#     pass