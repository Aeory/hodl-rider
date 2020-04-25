import unittest
from dateutil import parser

from models import Track, Line, Point


class TrackTestCase(unittest.TestCase):

    def test_track_point_conversions(self):
        track = Track(
            start_date=parser.parse('2020-01-01'),
            end_date=parser.parse('2020-01-02')
        )

        points = [
            Point(x=x, y=y) for x, y in
            [
                (-10, 20),
                (50, 25),
                (100, 40)
            ]
        ]
        track.points = points

        self.assertEqual(len(track.points), 3)

        self.assertEqual(len(track.lines), 2)

    def test_track_point_scaling(self):

        track = Track(
            x_scale=2,
            y_scale=2,
            start_date=parser.parse('2020-01-01'),
            end_date=parser.parse('2020-01-02')
        )

        points = [
            Point(x=x, y=y) for x, y in
            [
                (-10, 20),
                (50, 25)
            ]
        ]
        track.points = points

        self.assertEqual(len(track.points), 2)

        self.assertEqual(len(track.lines), 1)
