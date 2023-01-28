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
        self.api_url = 'http://api.aviationstack.com/v1/flights/'
        
    def get_data_from_api(self):
        # Get data from api
        api_result = requests.get(self.api_url, params=self.api_key)
        return api_result 
    
    def print_data_from_api(self):
        api_result = self.get_data_from_api()
        api_response = api_result.json()
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
        
       



