from asyncio.windows_events import NULL
import requests
import math
import json
import pprint as pprint
import time
import datetime
import os
import sys
import keys as keys


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
    
    def __init__(self, api_get, query_type='flight', detailed_query=NULL):
        self.api_get = api_get;
        self.query_type = query_type;
        self.detailed_query = detailed_query
        
        if(api_get == 'airlabs'):
            self.api_key = {'api_key': keys.AIRLABS_KEY}
            self.api_url = 'http://airlabs.co/api/v9/' + query_type
            # flight(default, airlines, airports, cities, fleets, routes, countries, timezones, taxes )
            
        elif(api_get == 'aviationstack'):
            self.api_key = {'access_key': keys.AVIATION_KEY}
            self.api_url = 'http://api.aviationstack.com/v1/' + query_type+'s'
            # flights(default), routes, airports, airlines, airplanes, aircraft_types , taxes, cities, countries
            
        else:
            print('Invalid api');
        
    def get_data_from_api(self):

        api_result = requests.get(self.api_url, self.api_key)
        api_response = api_result.json()
        
        def write_to_file(self):
            write_file = open(self.query_type + '.json', 'w')
            write_file.write(json.dumps(api_response))
            print(f'Data saved to {self.query_type} .json')   
            write_file.close()
            
          # Uncomment this 2 lines to save to file. 
          # write_to_file(self) 
        return api_response['response']
          #  print(i['name'] + " " + i['code'])
          #  print(i['code'])
    
   # def print_data_from_api(self):
   #     api_result = self.get_data_from_api()
   #     api_response = api_result.json()
   #     pprint.pprint(api_response)
        
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

        
            


countries_list = ApiConnector('airlabs', 'countries').get_data_from_api()
airports_list = ApiConnector('airlabs', 'airports').get_data_from_api()
cities_list = ApiConnector('airlabs', 'cities').get_data_from_api()
fleets_list = ApiConnector('airlabs', 'fleets').get_data_from_api()
airlines_list = ApiConnector('airlabs', 'airlines').get_data_from_api()
timezones_list = ApiConnector('airlabs', 'airlines').get_data_from_api()
taxes_list = ApiConnector('airlabs', 'taxes').get_data_from_api()

for i in countries_list:
    if i['name'] == "Yemen":
        print(i['code'])

for i in airports_list:
    print (i)

        
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


   function_result = (a_func*x**2) + (b_func*x) + c_func # quadratic equations result
   return  function_result / (s * plf)  * (1 - cf) * cw * (ef * m + p) + (af * x) + afm


def is_long_haul(flight_distance):
    # if flight_distance below 1500 mark as short haul
    if (flight_distance < 1500):
        return False
    else:
        return True



def calculate_distance(start_point, end_point):
    # start_point, end_point in format [latitude, longitude] can get that from airports api
    # Convertion to Radians so we can use math to check the distance
    def to_radians(degrees):
        return math.pi * degrees / 180


    EARTH_RADIUS = 6.371E3

    p1 = to_radians(start_point[0])
    p2 = to_radians(end_point[0])

    delta_p = to_radians(start_point[0] - end_point[0])
    delta_lambda = to_radians(start_point[1] - end_point[p1])

    calc =  math.sin(0.5 * delta_p)**2 + math.cos(p1) * math.cos(p2) * math.sin(0.5 * delta_lambda)**2
    c = 2 * math.atan2(math.sqrt(calc), math.sqrt(1 - calc))
    result = c * EARTH_RADIUS   #  result in KM
    return result
   

 

    """
•	At any given moment, what are the estimated total global CO2 emissions of all of the scheduled live flights currently in the air? 
o	Consider only those flights with specified departure and destination airports. 
•	What are the estimated global CO2 emissions over the last five years (2017-2022)?
o	What are the emissions for each year/month within that timeframe?
•	What are the top twenty most polluting routes globally, regionally (USA, Europe) and by country. 
o	Within each region and country, differentiate by domestic and international flights.
•	What are the total CO2 emissions by each Airline?
o	Within this, filter by routes and short-haul and long-haul.
•	What are the estimated CO2 emissions by airport?
o	Show a breakdown of both arrivals and departures and then short-haul and long-haul.
•	Top twenty countries responsible for aviation CO2 emissions. Filter by:
o	By domestic flights only.
o	By international flights only.
o	Combined CO2 emissions from domestic and international flights.
o	By country of aircraft registration.
•	Top twenty aircraft types responsible for the most CO2 emissions. 
 """ 

