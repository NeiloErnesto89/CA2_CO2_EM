# from django.test import TestCase
from services import *
# from Services.services import *
# import Services.services
import pytest

def test_example():
    assert 1 == 1

@pytest.mark.skip # skip as it's failing    
def test_example_fail():
    assert 2 == 1

@pytest.mark.xfail # as we anticpate failures     
def test_example_fail():
    assert 2 == 1
    
# @pytest.mark.slow # as we anticpate a 'slow' test   
# def test_example_fail():
#     assert 2 == 1 
   
# importing function from services and checking return functionality
def test_is_long_haul():
    assert is_long_haul(1499) == False
    assert is_long_haul(1500) == True
    assert is_long_haul(2000) == True


def test_calculate_co2_emissions():
    # assert Emissions.calculate_co2_emissions(1500) == type(int)
    
    cal_co2 = Emissions() # instantiate E cls
    # cal_co2.calculate_co2_emissions(1500)
    expected_emissions = 16.04
    assert cal_co2.calculate_co2_emissions(1500) == expected_emissions # true


# # Create your tests here.

# # from django.test import TestCase
# # from Services.services import Emissions

# # class EmissionsTestCase(TestCase):
# #     def setUp(self):
# #         Animal.objects.create(name="lion", sound="roar")
# #         Animal.objects.create(name="cat", sound="meow")

# #     def test_animals_can_speak(self):
# #         """Animals that can speak are correctly identified"""
# #         lion = Animal.objects.get(name="lion")
# #         cat = Animal.objects.get(name="cat")
# #         self.assertEqual(lion.speak(), 'The lion says "roar"')
# #         self.assertEqual(cat.speak(), 'The cat says "meow"')