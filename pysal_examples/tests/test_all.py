from unittest import TestCase

import pysal_examples

class TestHelpers(TestCase):
    def test_available(self):
        examples = pysal_examples.available()
        self.assertEqual(examples, ['10740', 'Line', 'Point', 'Polygon',
                                    'Polygon_Holes', 'arcgis', 'baltim',
                                    'book', 'burkitt', 'calemp', 'chicago',
                                    'columbus', 'desmith', 'geodanet',
                                    'juvenile', 'mexico', 'nat', 'networks',
                                    'newHaven', 'nyc_bikes', 'sacramento2',
                                    'sids2', 'snow_maps', 'south', 'stl',
                                    'street_net_pts', 'taz', 'us_income',
                                    'virginia', 'wmat'])
if __name__ == '__main__':
    unittest.main()
