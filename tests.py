# from django.test import TestCase
from app import *

# from Services.services import *
# from . import services
import haversine as hs
import pytest
import inspect
import json
import numpy as np
import keys as keys
import os
import time
import threading 


@pytest.mark.xfail(raises=AssertionError) # as we anticpate failures     
def test_example_fail():
    assert 2 == 1
    
@pytest.mark.xfail(raises=AssertionError)
def test_set_comparison():
    # decent use case if ==
    # AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
    set1 = set("3333")
    set2 = set("3334")
    assert set1 == set2

"""
GUI Builder Tests:
Here we are checking if the window size and title is correct.
Interestingly, the geometry overrides the min size so the window
is being rendered W*H*X*Y == 200x200x0x0 on a windows desktop. 
Perhaps it's something we can adjust

"""
def test_gui_window():
    gui_window = MainGUI() #instantiate GUI
    assert gui_window.winfo_width() == 200 #600x500
    assert gui_window.winfo_height() == 200
    assert str(gui_window.winfo_geometry()) == '200x200+0+0'
    assert gui_window.winfo_toplevel().title() == "Flight Pollution Calculator" 
    # assert gui_window.winfo_toplevel().minsize() == (300, 200)
    assert gui_window.grid_size() == (4, 6)
    
@pytest.mark.xfail()
def test_main_menu_callback():
    # gui_window = MainGUI()
    gui_choice1 = MainGUI().main_menu_callback("Check estimated emissions of all of the scheduled flights")
    # gui_window.main_menu
    assert gui_choice1.sub1_menu.cget("state") == "disabled"

@pytest.mark.xfail()   
def test_sub1_menu_callback():
    gui_choice1 = MainGUI()
    # gui_choice1.sub1_menu_callback("Check estimated emissions of all of the scheduled flights")
    gui_choice1 = gui_choice1.sub1_menu
    # assert gui_choice1.label1.text == "Flight Pollution Calculator"
    # assert gui_choice1._values[1] == "List all Airports"
    assert gui_choice1._command == MainGUI().main_menu_callback()
        

# @pytest.mark.xfail()   
def test_button_start_click():
    gui_window = MainGUI() #instantiate GUI
    gui_window.button_start_click()
    gui_window.main_menu_var = "Check estimated emissions of all of the scheduled flights"
    # assert gui_window == "Check estimated emissions of all of the scheduled flights"
    
    # choice = "Check estimated emissions of all of the scheduled flights"
    # checking that after selecting choice 1 the api response was called
    # assert ApiResponse().list_all_flights.call_count == 1
    

"""
Emissions Class:
Here we are checking testing the functionality of the Emissions class

"""
    
# importing function from services and checking return functionality
def test_is_long_haul():
    assert is_long_haul(1499) == False
    assert is_long_haul(1500) == True
    assert is_long_haul(2000) == True


def test_calculate_co2_emissions():
    # assert Emissions.calculate_co2_emissions(1500) == type(int)
    
    cal_co2 = Emissions() # instantiate E cls (create an instance of Emissions class)
    # cal_co2.calculate_co2_emissions(1500)
    expected_emissions = 16.04
    assert cal_co2.calculate_co2_emissions(1500) == expected_emissions # true

@pytest.mark.xfail # as we anticpate failures 
def test_calculate_distance_nonrounded_fail():
    # (45.7597, 4.8422), (48.8567, 2.3508)
    # distance = hs.haversine(40.748817, -73.985428) # NYC
    distance = hs.haversine((45.7597, 4.8422), (48.8567, 2.3508))
    calc_distance = Emissions() # instantiate E cls
    
    # this assertion will give us an error as we have not rounded the result
    assert calc_distance.calculate_distance((45.7597, 4.8422), (48.8567, 2.3508)) == distance


def test_calculate_distance():
    
    distance = hs.haversine((45.7597, 4.8422), (48.8567, 2.3508))
    distance_rounded = round(distance, 2)
    calc_distance = Emissions() # instantiate E cls
    
    # this assertion will give be a success as we have rounded to 2 decimal places
    assert calc_distance.calculate_distance((45.7597, 4.8422), (48.8567, 2.3508)) == distance_rounded


@pytest.mark.xfail # as we anticpate failures - THIS TEST WORKS WITH A RETURN VALUE BUT FUNC ONLY CURRENLY HAS PRINT STATEMENTS IN CONDITIONS   
def test_is_distance_long_or_short():
    
    distance_long_or_short = Emissions()
    assert distance_long_or_short.is_distance_long_or_short(1499) == False, "value is less than 1500"
    assert distance_long_or_short.is_distance_long_or_short(1500) == False, "value is less than 1500" 
    assert distance_long_or_short.is_distance_long_or_short(2000) == True, "value is greater than 1500"

"""
https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html 
Here we are using capsys to capture data printed to terminal in function 
that just has prints in conditionals   
"""
def test_is_distance_long_or_short_2(capsys):
    
    distance_long_or_short = Emissions()
    dis_long_short = distance_long_or_short.is_distance_long_or_short(1499) # short haul
    captured = capsys.readouterr()
    
    # captured_distance = dis_long_short.readouterr()
    assert captured.out == 'That was a short-haul flight.\n', "this function falls into shorthaul conditional and prints this out in cmd terminal"
    
    dis_long_short_2 = distance_long_or_short.is_distance_long_or_short(2000)
    captured_long = capsys.readouterr()
    assert captured_long.out == 'That was a long-haul flight.\n', "this function falls into longhaul conditional and prints this out in cmd terminal"
    

"""
Testing the ApiResponse class 
"""

def test_get_iata_code():
    apr = ApiResponse()
    apr_func = apr.get_iata_code()    
    # inspect returns true if obj is a generator (via yield from function)
    assert inspect.isgenerator(apr_func)
    
# def test_get_all_flights_country():
#     apr = ApiResponse()
#     apr_func = apr.get_all_flights_country()
#     assert isinstance(apr_func, apr) , "value returns True"

@pytest.mark.skip()
def test_get_all_flights_country():
    ApiConnector('airlabs', 'flights') # api = 
    flights = ApiResponse().get_all_flights_country()
    
    assert isinstance(flights, dict), "Flight should be a dictionary"
        
        
    

# Flights = ApiConnector('airlabs', 'flights',).get_data_from_api()

# PASSING 
def test_get_airport_name():
    get_airport_name = ApiResponse().get_airport_name("EGKK") # pass in ICAO code
    get_airport_name_2 = ApiResponse().get_airport_name("EIDW") # pass in ICAO code
    assert get_airport_name == "London Gatwick Airport", "returns London Gatwick Airport as its icao is EGKK "
    assert get_airport_name_2 == "Dublin Airport", "returns Dublin Airport as its icao is EIDW "
    
    
# have to rewrite tests to check functionality
# @pytest.mark.xfail()
def test_get_all_arrival_airport():
    pass 
    # ApiConnector('airlabs', 'flights') # pass in connector deets
    # api_con = ApiResponse()
    # api_con.get_all_arrival_airport() # object not iterable ..
    
    # ApiResponse().get_all_arrival_airport()
    
    # assert ap1 == False
    # if(['arr_icao'] == ['icao_code']):
    #     print(['lat'], ['lng'])
    
# have to rewrite tests to check functionality
@pytest.mark.xfail()
def test_get_all_departure_airport():
    api_con = ApiResponse()
    api_con.get_all_departure_airport() # object not iterable ..
    
    
def test_get_airport_cordinates():
    air_coord = ApiResponse().get_airport_cordinates('EDDL') 
    assert air_coord == (51.282829, 6.766503) #passed
    
def test_list_all_airports():
    pass

@pytest.mark.xfail()
def test_list_all_airlines(capsys):
    api_con = ApiResponse()
    api_dict = api_con.list_all_airlines()
    api_dict= dict(api_dict)
    api_dict_read = capsys.readouterr()

    # Checking the printed output -> fail
    assert "Ryanair" in api_dict_read.out

#threading test
# @pytest.mark.xfail()
def test_list_all_flights():
   
    api = ApiConnector('airlabs', 'flights') # api = 
    # ApiResponse().list_all_flights(api)
    
    t = threading.Thread(target=ApiResponse().list_all_flights(api))
    t.start()
    assert t.is_alive() # asserting the thread containing the func is still going!!
    t.join(timeout=3) # basically waiting got the thread to complete 
    if t.is_alive():
        t.terminate() # terminate the thread 


# connecting but printing too slow so we skip this
@pytest.mark.skip() 
# @pytest.mark.timeout(5)
def test_list_all_flights():
    
    response = ApiConnector('airlabs', 'flights').get_data_from_api()
    # lis_all_fl2 = ApiResponse().list_all_flights()
    # first_elem = response[0]
    # first_key = list(response.keys())[0]
    # first_value = response[first_key]
    # assert first_key == {'aircraft_icao': 'A20N', 'airline_iata': 'SU', 'airline_icao': 'AFL', 'alt': 10668} 
    assert isinstance(response, list)
    # assert isinstance(lis_all_fl2, list)


# connecting but printing too slow so we skip this
@pytest.mark.skip() 
# @pytest.mark.timeout(5)
def test_list_all_flights_2():
    # import numpy as np
    # start = time.time()
    # while True: 
    # ApiConnector('airlabs', 'flights')
    # lis_all_fl2 = ApiResponse().list_all_flights_2()
    # air_flight = ApiResponse()
    # air_flight.list_all_flights_2()
    
    # assert print(ApiResponse().list_all_flights_2()) == {'RU': 51.8}
    
    ApiConnector('airlabs', 'flights')
    assert ApiResponse().list_all_flights_2() == None
    
    # dict_key = list(lis_all_fl2.keys())[0]
    # assert dict_key == 'RU'
    # time.sleep(2)
    # pytest.fail(KeyboardInterrupt("User interrupted test"))
 
        
        # if time.time() - (start > 0.5):
        #     break
        
@pytest.mark.skip()       
# @pytest.mark.timeout(5) # setting a timeout for long running function
def test_list_flights_with_departure_airport():
    api_con = ApiResponse().list_flights_with_departure_airport('EDDL')
    # next(iter(api_con.items() ))
    assert next(iter(api_con.items() )) == {'api_key': 'xxxxxxxxxxxxxxxxxxxxxx'}
    # while True:
    #     if api_con:
    #         time.sleep(0.005)
    #         break
        
@pytest.mark.skip() 
def test_list_flights_with_arrival_airport():
    ApiConnector('airlabs', 'flights')   
    air_con = ApiResponse()
    # assert air_con.list_flights_with_arrival_airport("EGKK") == '(51.282829, 6.766503)' # [0:5] in loop


@pytest.mark.skip() 
def test_list_domestic_flights_by_region():
    # ApiConnector('airlabs', 'flights')   
    # air_con = ApiResponse()
    # list_domestic_flights_by_region(region_letter)
    domestic = ApiResponse().list_domestic_flights_by_region('ED')
    assert domestic[:10] == "Flight CO2 emissions is 25.9 kg"

def test_list_international_flights_by_region():
    ApiConnector('airlabs', 'flights')   
    # air_con = ApiResponse()
    # list_international_flights_by_region(region_letter) # one 2 letters

@pytest.mark.skip() 
def test_list_flights_by_region():
    # ApiConnector('airlabs', 'flights') 
    api = ApiResponse()
    # api.list_flights_by_region('ED', False)
    # list_flights_by_region(region_letter, is_domestic):
    #List flights by region (passing one or two letters)
    assert api.list_flights_by_region('ED', False) == None
    
    assert print(ApiResponse().list_flights_by_region('ED', True)) == "That was a short-haul flight."

@pytest.mark.skip() 
def test_list_flights_by_airline():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_flights_by_region('ED', False)
    #List flights by airline(airline) (passing airline name)

@pytest.mark.skip()
def test_list_all_flights_by_countries():
    ApiConnector('airlabs', 'flights', 'dep_icao,arr_icao,flight_number,flag,aircraft_icao')   
    assert ApiResponse().list_all_flights_by_countries() == True


@pytest.mark.skip()
def test_list_shorthaul_flights_by_countries():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_shorthaul_flights_by_countries()
    
@pytest.mark.skip()
def test_list_longhaul_flights_by_countries():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_shorthaul_flights_by_countries()

@pytest.mark.skip()
def test_list_domestic_flights_by_countries():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_domestic_flights_by_countries()

@pytest.mark.skip()
def test_list_international_flights_by_countries():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_international_flights_by_countries()

@pytest.mark.skip()
def test_list_flights_by_registration_country():
    ApiConnector('airlabs', 'flights')   
    ApiResponse().list_flights_by_registration_country()
     

@pytest.mark.skip() # datset too big
def test_list_flights_by_aircraft_type(capsys):
    # api_key = ApiConnector('airlabs', 'flights')
    ApiResponse().list_flights_by_aircraft_type()
    captured_aircraft = capsys.readouterr()
    output_aircraft = captured_aircraft.out.strip('\n') # {'A20N': 51.8}
    expect_aircraft = "{'A20N': 51.8}"
    assert str(output_aircraft) == str(expect_aircraft) # PASSING
    
    
@pytest.mark.skip() # datset too big
def test_list_top_polluted_routes():
    ApiConnector('airlabs', 'routes').save_routes('KJFK') # passing
    route = ApiResponse().list_top_polluted_routes()
    assert 'KJFK' in route

# def test_list_top_polluted_routes(capsys):    
#     api_key = ApiConnector('airlabs', 'flights')
#     api_key.print_api_key()
#     captured_api_key = capsys.readouterr()
#     output_api_key = captured_api_key.out.strip('\n')
#     expected_api_key = "{'api_key': '}"
#     assert str(output_api_key) == str(expected_api_key) # PASSING

### API Connector Class

def test_api_connector():
    api_get = 'airlabs'
    query_type = 'flight'
    detailed_query = {'detailed': True}
    
    api_con = ApiConnector(api_get, query_type, detailed_query)
    
    assert isinstance(api_con, ApiConnector)
    assert api_con.api_get == api_get , "value is api_get"
    assert api_con.query_type == query_type , "value is query type"
    assert api_con.detailed_query == detailed_query , "value is detailed query"
    
    
def test_save_routes():
    api_route = ApiConnector('airlabs', 'routes')
    api_route.save_routes('LAX')
    with open('routes.json', 'r') as read_file:
        json_data = json.load(read_file)
        
    new_route= {'route' : 'LAX'}
    json_data.append(new_route)    
    
    with open('routes.json', 'w') as f:
        json.dump(json_data, f)
    
    assert isinstance(json_data, list) # passing
    assert [{'route' : 'LAX'}] == json_data # passing

@pytest.mark.skip()  
def test_get_data_from_api():
    api_data = ApiConnector('airlabs', 'flights')
    api_response = api_data.get_data_from_api()
    
    assert isinstance(api_response, list)
    # assert [{'aircraft_icao': 'A320'}] in api_response # response too large
    
    # assert ApiConnector('airlabs', 'flights').get_data_from_api() is not 0

@pytest.mark.skip()  
def test_write_to_file():
    api_data = ApiConnector('airlabs', 'flights')
    api_data_1 = api_data.write_to_file()
    assert isinstance(api_data_1, np.ndarray)
    
def test_read_data_file():
    api_data = ApiConnector('airlabs', 'flights')
    api_data_1 = api_data.read_data_file()
    assert isinstance(api_data_1, np.ndarray) # multidimension via type check 

@pytest.mark.skip()   
def test_print_data_from_api(capsys):
    api_data = ApiConnector('airlabs', 'flights')
    api_data.print_data_from_api()
    captured_api_data = capsys.readouterr()
    expected_api_data = 200 # not return status code
    assert captured_api_data == expected_api_data
    
"""
https://docs.pytest.org/en/7.1.x/how-to/capture-stdout-stderr.html 
Here we are using capsys to capture data printed to terminal in function   
"""
def test_print_api_key(capsys):
    # api_get = 'airlabs'
    # query_type = 'flight'
    # detailed_query = {'detailed': True}
    # api_con = ApiConnector(api_get, query_type, detailed_query)
    # api_con = api_data = ApiConnector('airlabs', 'flights').print_api_key()
    # api_var = api_con.print_api_key()
    # api_key = api_con.print_api_key()
    api_key = ApiConnector('airlabs', 'flights')
    api_key.print_api_key()
    captured_api_key = capsys.readouterr()
    output_api_key = captured_api_key.out.strip()
    expected_api_key = "{'api_key': 'xxxxxxxxxx'}"
    assert str(output_api_key) == str(expected_api_key) # PASSING
    
@pytest.mark.skip()  
def test_check_server_is_running(capsys):
    api_server = ApiConnector('airlabs', 'flights')
    api_server.check_server_is_running()
    captured_server = capsys.readouterr()
    output_server = captured_server.out.strip()
    
    assert 'Server is running' in output_server
