import requests  
import json
from env import API_KEY 

"""
This class is dealing with the api connection from AirLabs
"""

class ApiConnection:
    
    def __init__(self) -> None:
        self.api_base = 'http://airlabs.co/api/v9/'
        self.search_type = 'flight'
        
    
    def get_airlab_api(self):
        params = {
            'api_key': API_KEY, # apikey
            # 'params1': 'value1' # value1
            }
        # params["_fields"] = 'dep_icao,arr_icao,flight_number,flag,aircraft_icao'
        method = 'flights'
        array_view = '?_view=array&_fields=dep_icao,arr_icao,flight_number,flag,aircraft_icao' # viable to change
        api_base = 'http://airlabs.co/api/v9/'
        api_result = requests.get(api_base+method+array_view, params) #timeout=0.5, stream=True
        # api_response = api_result.json()
        print(params)

        # some tester to parse the large quantities of data coming from the api
        api_response = json.loads(api_result.text)
        print(type(api_response))
        print(api_response[:20])

# print(Api_Connection.get_airlab_api())

apiCon = ApiConnection() # instantiate the class to obtain 'self'
apiCon.get_airlab_api()
        