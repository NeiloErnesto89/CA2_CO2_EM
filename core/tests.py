# # from django.test import TestCase
# # from services import *
# from Services.services import *
# import pytest

# def test_example():
#     assert 1 == 1

# @pytest.mark.skip # skip as it's failing    
# def test_example_fail():
#     assert 2 == 1


# @pytest.mark.xfail # as we anticpate failures     
# def test_example_fail():
#     assert 2 == 1
    
# # @pytest.mark.slow # as we anticpate failures     
# def test_example_fail():
#     assert 2 == 1

    
# # importing function from services and checking return functionality
# def test_is_long_haul():
#     assert is_long_haul(1499) == False
#     assert is_long_haul(1500) == True
#     assert is_long_haul(2000) == True


# # test_is_long_haul(1500)

# # def test_calculate_co2_emissions(flight_distance):

# #        if (test_is_long_haul(flight_distance)):
# #            s = 280.21
# #            plf = 0.82
# #            cf = 0.74
# #            a_func = 0.0001
# #            b_func = 7.104
# #            c_func = 5044.93
# #        else:
# #            s = 153.51
# #            plf = 0.82
# #            cf = 0.93
# #            a_func = 0
# #            b_func = 2.714
# #            c_func = 1166.52
        
# #        x = flight_distance
# #        cw = 2.40 
# #        ef = 3.15
# #        m = 2
# #        p = 0.54
# #        af = 0.00038
# #        afm = 11.68


# #        function_result = (a_func*x**2) + (b_func*x) + c_func # quadratic equations result
# #        rest_equation = (s * plf)  * (1 - cf) * cw * (ef * m + p) + (af * x) + afm
# #        result = function_result / rest_equation
# #        return round(result, 2)
   
# # # test_calculate_co2_emissions(1500)

# # # Create your tests here.

# # # from django.test import TestCase
# # # from Services.services import Emissions

# # # class EmissionsTestCase(TestCase):
# # #     def setUp(self):
# # #         Animal.objects.create(name="lion", sound="roar")
# # #         Animal.objects.create(name="cat", sound="meow")

# # #     def test_animals_can_speak(self):
# # #         """Animals that can speak are correctly identified"""
# # #         lion = Animal.objects.get(name="lion")
# # #         cat = Animal.objects.get(name="cat")
# # #         self.assertEqual(lion.speak(), 'The lion says "roar"')
# # #         self.assertEqual(cat.speak(), 'The cat says "meow"')