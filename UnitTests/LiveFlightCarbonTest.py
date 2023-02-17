import unittest

class LiveFlightCarbonTest(unittest.TestCase):

    def long_haul_co2(self):
         #Call long haul method
         
        self.assertEqual(850, 850)

    #def short_haul_c02(self):
    #     #Call long haul method
    #    self.assertEqual(850, 832)

        ### More methods
    def test_upper(self):
            self.assertEqual("dottie".upper(),"DOTTIE")

if __name__ == '__main__':
    unittest.main()