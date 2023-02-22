import unittest

class LiveFlightCarbonTest(unittest.TestCase):

    def haversine_Test(self):    
         #This is the Co2 example for JFK to DUB
        self.assertEqual(832, 832)

        ### More test methods
    def get_airport_name(self, airport_code):
        for i in self.airports_list.read_data_file():
            if (i.get('icao_code') == airport_code):
                return i['name']
        self.assertEqual('DUB','DUB')

if __name__ == '__main__':
    unittest.main()