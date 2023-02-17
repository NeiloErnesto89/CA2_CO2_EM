import unittest

class DistanceTest(unittest.TestCase):

    def haversine_Test(self):
         #Call long haul method
         #This is the Co2 example for JFK to DUB
        self.assertEqual(832, 832)

    def is_long_haul_true(self):
       # if flight_distance below 1500 mark as short haul
        self.assertTrue("Returned true");

    def is_long_haul_false(self):
       # if flight_distance greater 1500 mark as short haul

        self.assertTrue("Returned false");
        ## More methods

if __name__ == '__main__':
    unittest.main()