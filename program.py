import requests
import json
import pprint
import time
import datetime
import os
import sys

aviation_api_key  = '87589d7335551dbbde5ccef4eb116749'


class Emissions:
    

    def __init__(self, flight_number, departure_date, departure_airport, arrival_airport, airline):
        self.flight_number = flight_number
        self.departure_date = departure_date
        self.departure_airport = departure_airport
        self.arrival_airport = arrival_airport
        self.airline = airline

    def get_flight_number(self):
        return self.flight_number

    def get_departure_date(self):
        return self.departure_date

    def get_departure_airport(self):
        return self.departure_airport

    def get_arrival_airport(self):
        return self.arrival_airport

    def get_airline(self):
        return self.airline

    def get_emissions(self):
        # Get the emissions for the flight
        # Get the flight data
        # Get the aircraft type
        # Get the emissions for the aircraft type
        # Return the emissions
        return 0

    def get_aircraft_type(self):
        # Get the aircraft type for the flight
        # Return the aircraft type
        return 0

    def get_emissions_for_aircraft_type(self):
        # Get the emissions for the aircraft type
        # Return the emissions
        return 0

    def get_flight_data(self):
        # Get the flight data from the API
        # Return the flight data
        return 0

    def get_flight_data_from_api(self):
        # Get the flight data from the API
        # Return the flight data
        return 0

    def get_flight_data_from_file(self):
        # Get the flight data from the file
        # Return the flight data
        return 0

    def get_flight_data_from_database(self):
        # Get the flight data from the database
        # Return the flight data
        return 0

    def get_flight_data_from_user(self):
        # Get the flight data from the user
        # Return the flight data
        return 0

    def get_flight_data_from_api(self):
        # Get the flight data directly from api
        # Return the flight data
       return 0
    
   
class ApiConnector:
    
    def __init__(self, api_key):
        self.api_key = {'access_key': api_key}
        self.api_url = 'http://api.aviationstack.com/v1/flights'
        
    def get_data_from_api(self):
        # Get data from api
        api_result = requests.get(self.api_url, params=self.api_key)
        return api_result 
    
    def print_data_from_api(self):
        api_result = self.get_data_from_api()
        api_response = api_result.json()
        print(api_response)
        pprint.pprint(api_response)
        
    def print_api_key(self):
        # print api key
        print(self.api_key)

    def check_server_is_running(self):
        # Check server 
        api_result = self.get_data_from_api()
        print(api_result.status_code)
        if api_result.status_code == 200:
            print('Server is running')
        else:
            print('Server is not running')

        

        
ApiConnector(aviation_api_key).print_api_key()
ApiConnector(aviation_api_key).print_data_from_api()
ApiConnector(aviation_api_key).check_server_is_running()
        
       




# To Be Added Somewhere Later
# Co2 Formula

def calculate_co2_emissions(flight_distance):
   """
   The following formula is used to calculate the total CO2-equivalent emissions:
   𝑬 = ()𝒂𝒙 𝟐 +𝒃𝒙 +𝒄 / 𝑺 ∗ 𝑷𝑳𝑭) ∗ (𝟏 −𝑪𝑭) ∗ 𝑪𝑾 ∗ (𝑬𝑭 ∗ 𝑴 + 𝑷)+ 𝐀𝐅 ∗ 𝐱 + �
   # s = number_of_seats # Shorthaul -> 153.51 , Longhaul -> 280.21
   # plf = passenger_load_factor # Shorthaul -> 0.82 ,  Longhaul -> 0.82 
   # cf = cargo_factor # Shorthaul -> 0.93 ,  Longhaul -> 0.74 
   """
   
   if (is_long_haul(flight_distance)):
       s = 280.21
       plf = 0.82
       cf = 0.74
       a_func = 0.0001
       b_func = 7.104
       c_func = 5044.93
   else:
       s = 153.51
       plf = 0.82
       cf = 0.93
       a_func = 0
       b_func = 2.714
       c_func = 1166.52
        
   x = flight_distance

   cw = 2.40 
   ef = 3.15
   m = 2
   p = 0.54
   af = 0.00038
   afm = 11.68


   function_result = (a_func*x**2) + (b_funct*x) + c_func # quadratic equations result
   return  function_result / (s * plf)  * (1 - cf) * cw * (ef * m + p) + (af * x) + amf


def is_long_haul(flight_distance):
    # if flight_distance below 1500 mark as short haul
    if (flight_distance < 1500):
        return False
    else:
        return True


    