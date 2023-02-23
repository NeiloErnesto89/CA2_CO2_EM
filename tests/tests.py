# from django.test import TestCase
from services import *
# from Services.services import *
# import Services.services
import haversine as hs
import pytest
import inspect
# import math

def test_example():
    assert 1 == 1

@pytest.mark.skip # skip as it's failing    
def test_example_fail():
    assert 2 == 1

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
    
def test_is_distance_long_or_short():
    
    distance_long_or_short = Emissions()
    assert distance_long_or_short.is_distance_long_or_short(1499) == False, "value is less than 1500"
    assert distance_long_or_short.is_distance_long_or_short(1500) == False, "value is less than 1500" 
    assert distance_long_or_short.is_distance_long_or_short(2000) == True, "value is greater than 1500"
    

# class TestApiResponse:
    
#     def test_init(self):
#         obj = ApiResponse()
#         assert isinstance(obj, ApiResponse)

def test_get_iata_code():
    apr = ApiResponse()
    apr_func = apr.get_iata_code()
    # assert isinstance(cf_func, )
    # assert isinstance(cf_func, list)
    
    # inspect returns true if obj is a generator (via yield from function)
    assert inspect.isgenerator(apr_func)
    
# def test_get_all_flights_country():
#     apr = ApiResponse()
#     apr_func = apr.get_all_flights_country()
    # assert isinstance(cf_func, )
    # assert isinstance(apr_func, list), "value returns list elements"
