# from django.test import TestCase
from app import *

# from Services.services import *
# from . import services
import haversine as hs
import pytest
import inspect
import json
import numpy as np
import os

# def test_example():
#     assert 1 == 1

"""
GUI Builder Tests:
Here we are checking if the window size and title is correct.
Interestingly, the geometry overrides the min size so the window
is being rendered W*H*X*Y == 200x200x0x0 on a windows desktop. 
Perhaps it's something we can adjust

"""
def test_gui_window():
    gui_window = MainGUI() #instantiate GUI
    assert gui_window.winfo_width() == 200
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
    
    
# def test_button_start_click(gui_auto):
#     import pyautogui
#     gui_auto.main_menu_var.set("Check estimated emissions of all of the scheduled flights")
    
#     #invoke pyautogui
#     pyautogui.click(gui_aut)
#     time.sleep(0.5)
#     assert gui_auto.choice == "Check estimated CO2 emissions over the last five years"
    
    # gui_window = MainGUI() #instantiate GUI
    
    # var = gui_window.button_start_click()
@pytest.mark.xfail()   
def test_button_start_click():
    gui_window = MainGUI() #instantiate GUI
    gui_window.main_menu_var = "Check estimated emissions of all of the scheduled flights"
    assert gui_window == "Check estimated emissions of all of the scheduled flights"
    
    
    
    # choice = "Check estimated emissions of all of the scheduled flights"
    # checking that after selecting choice 1 the api response was called
    assert ApiResponse().list_all_flights.call_count == 1
    

@pytest.mark.xfail(raises=AssertionError) # as we anticpate failures     
def test_example_fail():
    assert 2 == 1
    
# @pytest.mark.slow # as we anticpate a 'slow' test   
# def test_example_fail():
#     assert 2 == 1 

@pytest.mark.xfail(raises=AssertionError)
def test_set_comparison():
    # decent use case if ==
    # AssertionError: assert {'0', '1', '3', '8'} == {'0', '3', '5', '8'}
    set1 = set("3333")
    set2 = set("3334")
    assert set1 == set2
    
   
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
    

# class TestApiResponse:
    
#     def test_init(self):
#         obj = ApiResponse()
#         assert isinstance(obj, ApiResponse)

def test_get_iata_code():
    apr = ApiResponse()
    apr_func = apr.get_iata_code()    
    # inspect returns true if obj is a generator (via yield from function)
    assert inspect.isgenerator(apr_func)
    
# def test_get_all_flights_country():
#     apr = ApiResponse()
#     apr_func = apr.get_all_flights_country()
#     assert isinstance(apr_func, apr) , "value returns True"

# PASSING 
def test_get_airport_name():
    get_airport_name = ApiResponse().get_airport_name("EGKK") # pass in ICAO code
    get_airport_name_2 = ApiResponse().get_airport_name("EIDW") # pass in ICAO code
    assert get_airport_name == "London Gatwick Airport", "returns London Gatwick Airport as its icao is EGKK "
    assert get_airport_name_2 == "Dublin Airport", "returns Dublin Airport as its icao is EIDW "
    
    
# have to rewrite tests to check functionality
@pytest.mark.xfail()
def test_get_all_arrival_airport():
    api_con = ApiResponse()
    api_con.get_all_arrival_airport() # object not iterable ..
    # assert ap1 == False
    # if(['arr_icao'] == ['icao_code']):
    #     print(['lat'], ['lng'])
    
# have to rewrite tests to check functionality
@pytest.mark.xfail()
def test_get_all_departure_airport():
    api_con = ApiResponse()
    api_con.get_all_departure_airport() # object not iterable ..

def test_list_all_airlines():
    api_con = ApiResponse()

def test_list_all_flights():
    pass

def test_list_all_flights_2():
    pass

def test_list_flights_with_departure_airport():
    pass

def test_list_flights_with_arrival_airport():
    pass

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