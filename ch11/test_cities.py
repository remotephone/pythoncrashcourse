from cities import place_name
import unittest

class PlaceTestCase(unittest.TestCase):
    """Tests for 'cities.py'"""

    def test_place_names(self):
        """ Do names like London, England work?"""
        place = place_name('london', 'england', '10000')
        self.assertEqual(place, 'London, England - Pop: 10000')


unittest.main()