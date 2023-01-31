import requests  
from env import API_KEY 

"""

26/01/23: (Neil) this is just an early tester to play around with the apis
for CA2 (contem_software)
idea: https://www.geodose.com/2020/08/create-flight-tracking-apps-using-python-open-data.html
"""

import requests
import json
import pprint

params = {
  'api_key': API_KEY, # apikey
  'params1': 'value1' # value1
}
method = 'flights'
array_view = '?_view=array&_fields=hex,flag,lat,lng,dir,alt' # viable to change
api_base = 'http://airlabs.co/api/v9/'
api_result = requests.get(api_base+method+array_view, params) #timeout=0.5, stream=True
# api_response = api_result.json()

# some tester to parse the large quantities of data coming from the api
api_response = json.loads(api_result.text)
print(type(api_response))
print(api_response[:20])

num = 4
sorted_list = [x for index, x in enumerate(api_response) if index < num] # fyi - this is a list comprehension 
print(sorted_list[:1]) # returns first elem(list) within list


# print(json.dumps(api_response, indent=4, sort_keys=True ))

# limit = json.dumps(api_response, indent=4, sort_keys=True )



# define class
    
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