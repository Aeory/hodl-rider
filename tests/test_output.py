import unittest
from tests.data.export_test_data import example_track
import json
from utils.export_to_json import track_to_json

class ExportJsonTestCase(unittest.TestCase):
    def test_export(self):



        with open('data/export_example_1.json', 'r') as file:
         expected_output = json.load(file)



        self.assertEqual(True, expected_output)

