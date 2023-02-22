# from django.test import TestCase
# from Services.services import Emissions

import pytest

def test_example():
    assert 1 == 1
    
def test_example_fail():
    assert 2 == 1


# Create your tests here.

# from django.test import TestCase
# from Services.services import Emissions

# class EmissionsTestCase(TestCase):
#     def setUp(self):
#         Animal.objects.create(name="lion", sound="roar")
#         Animal.objects.create(name="cat", sound="meow")

#     def test_animals_can_speak(self):
#         """Animals that can speak are correctly identified"""
#         lion = Animal.objects.get(name="lion")
#         cat = Animal.objects.get(name="cat")
#         self.assertEqual(lion.speak(), 'The lion says "roar"')
#         self.assertEqual(cat.speak(), 'The cat says "meow"')