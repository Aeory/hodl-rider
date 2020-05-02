import unittest
from tests.data.export_test_data import example_track
import json
from export.export_to_json import track_to_json
import os


class ExportJsonTestCase(unittest.TestCase):
    def test_export(self):

        filename = "test-output"
        track_to_json(example_track)

        with open("data/export_example_1.json", "r") as file:
            expected_output = json.load(file)

        with open("test-output.json", "r") as file:
            output = json.load(file)
            os.remove(file.name)
        self.assertEqual(output, expected_output)
