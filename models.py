import math
from dataclasses import dataclass
from datetime import date
from typing import List


class Track:
    """Total track, including scales and date ranges.

    Attributes:
        start_date: datetime
        end_date: datetime
        points: List of lines

    """

    def __init__(
            self,
            start_date: date,
            end_date: date,
            x_scale: float = 1,
            y_scale: float = 0.001,
            ticker: str = "BTC",
            points=List['Point']
    ):
        self.start_date = start_date
        self.end_date = end_date
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.ticker = ticker
        self.points: List[Point] = points


@dataclass
class Point:
    x: float
    y: float


@dataclass
class Line:
    """A single line segment, connecting two points on a track

    Attributes:
        point_a: tuple of (x, y)
        point_b: tuple of (x, y)

    Methods:
        len(line) returns the length of the line segment from point_a to point_b

    """
    point_a: Point
    point_b: Point

    def __len__(self):
        return math.sqrt((self.point_b[1] - self.point_a[1])**2 + (self.point_b[1] - self.point_a[1])**2)