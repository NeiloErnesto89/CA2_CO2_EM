﻿"""
    This is the main file of the program. It contains the main function and the author which is
    bloobsky
"""

import requests
import json
import pprint as pprint
import haversine as hs
import keys as keys
import numpy as np


def is_long_haul(flight_distance):
        # if flight_distance below 1500 mark as short haul
    if (flight_distance < 1500):
        return False
    else:
        return True 

class Emissions:
        
      
    def calculate_co2_emissions(self, flight_distance):

        
    # The following formula is used to calculate the total CO2-equivalent emissions:
    # 𝑬 = ()𝒂𝒙 𝟐 +𝒃𝒙 +𝒄 / 𝑺 ∗ 𝑷𝑳𝑭) ∗ (𝟏 −𝑪𝑭) ∗ 𝑪𝑾 ∗ (𝑬𝑭 ∗ 𝑴 + 𝑷)+ 𝐀𝐅 ∗ 𝐱 + �
   #E: CO2-eq emissions per passenger [kg]
   #x: Flight Distance [km] which is defined as the sum of GCD, the great circle distance, and DC, a distance
   #correction for detours and holding patterns, and inefficiencies in the air traffic control systems [km]
   #S: Average number of seats (total across all cabin classes)
   #PLF: Passenger load factor
   #CF: Cargo factor
   #CW: Cabin class weighting factor
   #EF: CO2 emission factor for jet fuel combustion (kerosene)
   #M: Multiplier accounting for potential non-CO2 effects
   #P: CO2e emission factor for preproduction jet fuel, kerosene
   #AF: Aircraft factor
   #A: Airport infrastructure emissions
   #The part ax
   #2 + bx + c is a nonlinear approximation of f(x) + LTO
   #LTO: Fuel consumption during landing and takeoff cycle including taxi [kg]



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
       rest_equation = (s * plf)  * (1 - cf) * cw * (ef * m + p) + (af * x) + afm
       result = function_result / rest_equation
       return round(result, 2)

       
    def calculate_distance(self, departure_lat_lng, arrival_lat_lng):
        # Calculate distance
        distance = hs.haversine(departure_lat_lng, arrival_lat_lng)
      #  print(f'Total distance is {round(distance, 2)} kilometeres, but full distance is {distance}')
        return round(distance, 2)

    def is_distance_long_or_short(self, distance):
        if(distance > 1500):
            print(f'That was a long-haul flight.')
        else:
            print(f'That was a short-haul flight.')


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
        self.flights_list = ApiConnector('airlabs', 'flights', 'dep_icao,arr_icao,flight_number,flag,aircraft_icao')
        self.countries_list = ApiConnector('airlabs', 'countries')
        self.airports_list = ApiConnector('airlabs', 'airports', 'icao_code,lat,lng')
        self.cities_list = ApiConnector('airlabs', 'cities')
        self.fleets_list = ApiConnector('airlabs', 'fleets')
        self.airlines_list = ApiConnector('airlabs', 'airlines')
        self.timezones_list = ApiConnector('airlabs', 'airlines')
        self.taxes_list = ApiConnector('airlabs', 'taxes')

    
    def get_all_flights_country(self):
        # Get all flights by country
        for i in self.flights_list:
            try:
                print(i['flag'])
            except:
                pass
            
    def get_airport_name(self, airport_code):
        # Get airport name based on icao_code
        for i in self.airports_list.read_data_file():
            if (i.get('icao_code') == airport_code):
                return i['name']

    def get_all_arrival_airport(self):
        # Get arrival airport based on icao_code
        print("Arrival Lang Lat")
        for i in self.flights_list:
            for j in self.airports_list:
                try:
                    if(i['arr_icao'] == j['icao_code']):
                        print(j['lat'], j['lng'])
                except:
                    pass   
    
    def get_all_departure_airport(self):
        # Get all airports latitute and longtitude
        print("Departure Lang Lat")
        for i in self.flights_list:
            if(i.get('dep_icao') and i.get('arr_icao')):
                for j in self.airports_list: 
                        try:
                            if(i['dep_icao'] == j['icao_code']):
                                print(j['lat'], j['lng'])
                                break;
                        except:
                            pass
                
    def get_airport_cordinates(self, airport_name):
        # Get airport cordinates based on icao_code
        for i in self.airports_list.read_data_file():
            if(i.get('icao_code') == airport_name):               
                return i['lat'], i['lng']

    def list_all_airlines(self):
        # List all airlines
        for i in self.airlines_list:
            try:
                print(i['name'])
            except:
                pass
            
    def list_all_airports(self):
        for i in self.airports_list.read_data_file():
            if(i.get('icao_code') and i.get('name')):
                print(f'Airport name is {i["name"]} and the airport code is {i["icao_code"]} ')

            
    def list_all_flights(self):
        total_result = 0 
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                print(f"Flight Number is {i['flight_number']} and the airline is {i['flag']} and the aircraft is {i['aircraft_icao']} going from {i['dep_icao']} to {i['arr_icao']}");
                print(f'Flight distance is {Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"]))} km');
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                print(f'{result} kg CO2 emitted into the atmosphere.')
                total_result += result
                print(f'Total consumption so far is {round(total_result, 2)} KG  per passenger ')
            else:
                print("No data available for this one")


    def list_flights_with_departure_airport(self, airport_icao):
        total_result = 0
        for i in self.flights_list.get_data_from_api():
            if(i.get('dep_icao') == airport_icao):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                total_result += result
                print(f'Total consumption from {ApiResponse().get_airport_name(airport_icao)} so far is {round(total_result, 2)} kg ')


    def list_flights_with_arrival_airport(self, airport_icao):
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('arr_icao') == airport_icao):
                filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                total_result += result
                print(f'Total consumption from {ApiResponse().get_airport_name(airport_icao)} so far is {round(total_result, 2)} kg ')

    
    def list_domestic_flights_by_region(self, region_letter):
        #List domestic flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) == i['arr_icao'].startswith(region_letter)):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {ApiResponse().get_airport_name(region_letter)} so far is {round(total_result, 2)} kg ')

    def list_international_flights_by_region(self, region_letter):
        #List international flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) != i['arr_icao'].startswith(region_letter)):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {ApiResponse().get_airport_name(region_letter)} so far is {round(total_result, 2)} kg ')
        
                
                
    def list_flights_by_region(self, region_letter, short_haul):
        #List flights by region (passing one or two letters)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('dep_icao') and i.get('arr_icao')):
                if(i['dep_icao'].startswith(region_letter) and i['arr_icao'].startswith(region_letter)):
                    filter_long_short_haul = Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao']))
                    if(short_haul == True and filter_long_short_haul < 1500):
                        
                        print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        total_result += result
                        print(f'Total consumption from {region_letter} so far is {round(total_result, 2)} kg ')
                    elif(short_haul == False and filter_long_short_haul > 1500):
                        print(f"Flight Number is {i['flight_number']} and the airline is {i['flag']} and the aircraft is {i['aircraft_icao']} going from {i['dep_icao']} to {i['arr_icao']}");
                        print(f'Flight distance is {Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"]))} km');
                        print(Emissions().is_distance_long_or_short(filter_long_short_haul))
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        total_result += result
                        print(f'Total consumption from {region_letter} so far is {round(total_result, 2)} kg ')

    def list_flights_by_airline(self, airline):
        #List flights by airline (passing airline name)
        total_result = 0
        for i in self.flights_list.read_data_file():
            if(i.get('airline_name')):
                if(i['airline_name'] == airline):
                        result = Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i['dep_icao']), ApiResponse().get_airport_cordinates(i['arr_icao'])))
                        print(f'Flight CO2 emissions is {Emissions().calculate_co2_emissions(Emissions().calculate_distance(ApiResponse().get_airport_cordinates(i["dep_icao"]),  ApiResponse().get_airport_cordinates(i["arr_icao"])))} kg');
                        total_result += result
                        print(f'Total consumption from {airline} so far is {round(total_result, 2)} kg ')
     
   
class ApiConnector:
    
    def __init__(self, api_get, query_type='flight', detailed_query=None):
        self.api_get = api_get;
        self.query_type = query_type
        self.detailed_query = detailed_query
        
        if(api_get == 'airlabs'):
            self.api_key = {'api_key': keys.AIRLABS_KEY}
            self.api_url = 'http://airlabs.co/api/v9/' + query_type
            
           # if(self.detailed_query != None):
            #    self.api_key['_fields'] = detailed_query
            # flight(default, airlines, airports, cities, fleets, routes, countries, timezones, taxes )
            
        elif(api_get == 'aviationstack'):
            self.api_key = {'access_key': keys.AVIATION_KEY}
            self.api_url = 'http://api.aviationstack.com/v1/' + query_type+'s'
            # flights(default), routes, airports, airlines, airplanes, aircraft_types , taxes, cities, countries
            
        else:
            print('Invalid api')
        
                
    def get_data_from_api(self):
        params = {'api_key':  keys.AIRLABS_KEY }
        params["_fields"]= self.detailed_query
        api_result = requests.get(self.api_url, params)
        api_response = api_result.json()
            
        return api_response['response']

    def write_to_file(self):
        params = {'api_key':  keys.AIRLABS_KEY }
        params["_fields"]= self.detailed_query
        api_result = requests.get(self.api_url, params)
        api_response = api_result.json()
        
        with open(self.query_type + '.json', 'w') as write_file: 
            write_file.write(json.dumps(api_response['response']))
        print(f'Data saved to {self.query_type} .json')   

    def read_data_file(self):
        with open(self.query_type + '.json', 'r') as read_file:
            data = np.array(json.load(read_file))
            return data
    
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
 
    
  #  Flights = ApiConnector('airlabs', 'flights',).get_data_from_api()
   # print(Flights)
    
    #Print Flight Flag
   # ApiResponse().get_all_flights_country()
    
    #Print Airport Coordinates
   # print(ApiResponse().get_airport_cordinates('EDDL'));
   # print(ApiResponse().get_airport_cordinates('EDDF'));
    #Calculate distanse
   # result =  Emissions().calculate_distance(ApiResponse().get_airport_cordinates('EDDL'),  ApiResponse().get_airport_cordinates('EDDF'))
   # print(str(Emissions().calculate_co2_emissions(result)) + " co2 emissions for that flight !");
  #  ApiConnector('airlabs', 'flights', 'dep_icao,arr_icao,flight_number,flag,aircraft_icao').write_to_file()
    ApiConnector('airlabs', 'flights').get_data_from_api()
    # All Flights - q1 --add en-route for flights live. 
   #ApiResponse().list_all_flights();
   # print(ApiResponse().get_all_departure_airport());

   # Get Emissions by Airport

#    print(ApiResponse().list_flights_with_departure_airport('EDDL'))
   # print(ApiResponse().list_flights_with_departure_airport('EDDF'))
    
    # List all airports
    #print(ApiResponse().list_all_airports())
    
  #List by country - domestic
   # ApiResponse().list_flights_by_region('ED', False)
   # ApiResponse().list_domestic_flights_by_region('ED')

   #List by country - international
    ApiResponse().list_international_flights_by_region('ED')
        

"""

1	At any given moment, what are the estimated total global CO2 emissions of all of the scheduled live flights currently in the air? 
1	Consider only those flights with specified departure and destination airports.   --> DONE
2	What are the estimated global CO2 emissions over the last five years (2017-2022)? --  Pandas
3	What are the emissions for each year/month within that timeframe? -- Pandas
4	What are the top twenty most polluting routes globally, regionally (USA, Europe) and by country. --> Pandas
5	Within each region and country, differentiate by domestic and international flights.  --> DONE
6	What are the total CO2 emissions by each Airline? --> "flag": "US", no problem with --> DONE
6	Within this, filter by routes and short-haul and long-haul. --> function ready !!
7	What are the estimated CO2 emissions by airport? --> dep_icao(out of flights) == icao_code DONE
7	Show a breakdown of both arrivals and departures and then short-haul and long-haul. () DONE (2 seperate function for arrival or departures)
7	What are the top twenty countries responsible for aviation CO2 emissions. --> "country_code": "US", no problem with
•	Top twenty countries responsible for aviation CO2 emissions. Filter by:
o	By domestic flights only.
o	By international flights only.
o	Combined CO2 emissions from domestic and international flights.
o	By country of aircraft registration.
•	Top twenty aircraft types responsible for the most CO2 emissions. 
""" 

