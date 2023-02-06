import requests
import math
import json
import pprint as pprint
import time
import datetime
import os
import sys
import haversine as hs
import keys as keys


def is_long_haul(flight_distance):
        # if flight_distance below 1500 mark as short haul
    if (flight_distance < 1500):
        return False
    else:
        return True 

class Emissions:
        
      
    def calculate_co2_emissions(flight_distance):

        
    # The following formula is used to calculate the total CO2-equivalent emissions:
    # 𝑬 = ()𝒂𝒙 𝟐 +𝒃𝒙 +𝒄 / 𝑺 ∗ 𝑷𝑳𝑭) ∗ (𝟏 −𝑪𝑭) ∗ 𝑪𝑾 ∗ (𝑬𝑭 ∗ 𝑴 + 𝑷)+ 𝐀𝐅 ∗ 𝐱 + �
    # s = number_of_seats # Shorthaul -> 153.51 , Longhaul -> 280.21
    # plf = passenger_load_factor # Shorthaul -> 0.82 ,  Longhaul -> 0.82 
    # cf = cargo_factor # Shorthaul -> 0.93 ,  Longhaul -> 0.74 

   
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

       
    def calculate_distance(self, departure_lat_lng, arrival_lat_lng):
        # Calculate distance
        distance = hs.haversine(departure_lat_lng, arrival_lat_lng)
        print(f'Total distance is {round(distance, 2)} kilometeres, but full distance is {distance}')
        return distance

"""   
Not gonna be used but shows the calculations. 
    def calculate_distance(self, start_point, end_point):
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
    

class ApiResponse:
    

    def __init__(self):
        self.flights_list = ApiConnector('airlabs', 'flights').get_data_from_api()
        self.countries_list = ApiConnector('airlabs', 'countries').get_data_from_api()
        self.airports_list = ApiConnector('airlabs', 'airports').get_data_from_api()
        self.cities_list = ApiConnector('airlabs', 'cities')
        self.fleets_list = ApiConnector('airlabs', 'fleets')
        self.airlines_list = ApiConnector('airlabs', 'airlines')
        self.timezones_list = ApiConnector('airlabs', 'airlines')
        self.taxes_list = ApiConnector('airlabs', 'taxes')

    
    def get_all_flights_country(self):
        for i in self.flights_list:
            try:
                print(i['flag'])
            except:
                pass

    def get_all_arrival_airport(self):
        print("Arrival Lang Lat")
        for i in self.flights_list:
            for j in self.airports_list:
                try:
                    if(i['arr_icao'] == j['icao_code']):
                        print(j['lat'], j['lng'])
                except:
                    pass   
    
    def get_all_departure_airport(self):
        print("Departure Lang Lat")
        for i in self.flights_list:
            for j in self.airports_list:
                try:
                    if(i['dep_icao'] == j['icao_code']):
                        print(j['lat'], j['lng'])
                except:
                    pass
                
    def get_airport_cordinates(self, airport_name):
        for i in self.airports_list:
            try:
                if(i['icao_code'] == airport_name):               
                    return i['lat'], i['lng']
            except:
                pass

            
""" To Be Continued
    def get_departure_lat_lng(self, departure_airport):
        # Get departure lat and lng from airports api
        for i in self.airports_list.get_data_from_api():
            try:
                if(i['iata_code'] == departure_airport):
                    return i['lat', 'lng']
            except:
                print("Error geting departure latitue and longtitude")
                
    def get_arrival_lat_lng(self, arrival_airport):
        # Get arrival lat and lng from airports api
        for i in self. airports_list.get_data_from_api():
            try:
                if(i['iata_code'] == arrival_airport):
                    return i['lat', 'lng']
            except:
                print("Error geting arrival latitue and longtitude")
"""
   
class ApiConnector:
    
    def __init__(self, api_get, query_type='flight', detailed_query=None):
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
            write_file.write(json.dumps(api_response['response']))
            print(f'Data saved to {self.query_type} .json')   
            write_file.close()   
            # Uncomment this 2 lines to save to file. 
            # write_to_file(self) 
        return api_response['response']

    
    def print_data_from_api(self):
        api_result = self.get_data_from_api()
        api_response = api_result.json()
        pprint(api_response)
        
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

        

# Program starts here
if __name__ == "__main__":
 

    #Print Flight Flag
    ApiResponse().get_all_flights_country()
    #Print Airport Coordinates
    print(ApiResponse().get_airport_cordinates('EDDL'));
    print(ApiResponse().get_airport_cordinates('EDDF'));
    #Calculate distanse
    Emissions().calculate_distance(ApiResponse().get_airport_cordinates('EDDL'),  ApiResponse().get_airport_cordinates('EDDF'))
    

        

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

