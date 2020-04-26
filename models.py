import math
from dataclasses import dataclass
from datetime import date
from typing import List
from random import random
import settings


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
            y_scale: float = 100,
            ticker: str = "BTC",
            points: List['Point'] = None,
            smoothing_coefficient: int = settings.SMOOTHING['coefficient']
    ):
        if not x_scale or not y_scale:
            raise ValueError("x-scale and y-scale values must be non-zero")
        self.x_scale = x_scale
        self.y_scale = y_scale
        self.start_date = start_date
        self.end_date = end_date
        self.ticker = ticker
        self.points: List[Point] = points or []
        self._lines: List[Line] = []
        self._smoothed_lines: List[Line] = []
        self._smoothing_coefficient = smoothing_coefficient
        self._starting_acceleration_lines = settings.STARTING_ACCELERATION_LINES
        self._smoothing_algorithm = settings.SMOOTHING['type']

    @property
    def lines(self):
        """Scaled lines from the input points.

        Note: len(lines) == len(points) - 1.
        """
        if not self._lines:
            if len(self.points) < 2:
                raise ValueError('Not enough points to create lines')
            last_point = self.points[0]
            for point in self.points[1:]:
                self._lines.append(
                    Line(
                        point_a=last_point.rescale(
                            x_scale=self.x_scale,
                            y_scale=self.y_scale
                        ),
                        point_b=point.rescale(
                            x_scale=self.x_scale,
                            y_scale=self.y_scale
                        ),
                        type=LineType.SCENERY
                    )
                )
                last_point = point
        return self._lines

    @property
    def smoothed_lines(self):
        if self._smoothing_algorithm != 'ROLLING_AVERAGE':
            raise NotImplementedError()

        if not self._smoothed_lines:
            if len(self.points) < self._smoothing_coefficient:
                raise ValueError('Not enough points to create smoothed lines')

            last_point = self.points[0]
            for i in range(self._smoothing_coefficient - 1, len(self.points)):
                last_n_points = self.points[i - (self._smoothing_coefficient - 1): i + 1]

                averaged_point = Point(
                    x=sum([point.x for point in last_n_points]) / self._smoothing_coefficient,
                    y=sum([point.y for point in last_n_points]) / self._smoothing_coefficient,
                    date_recorded=self.points[i].date_recorded
                )
                self._smoothed_lines.append(
                    Line(
                        point_a=last_point.rescale(
                            x_scale=self.x_scale,
                            y_scale=self.y_scale
                        ),
                        point_b=averaged_point.rescale(
                            x_scale=self.x_scale,
                            y_scale=self.y_scale
                        ),
                    )
                )
                last_point = averaged_point
            self._calculate_acceleration()
        return self._smoothed_lines

    def _calculate_acceleration(self):
        for line in self._smoothed_lines[:self._starting_acceleration_lines]:
            line.type = LineType.ACCELERATION
        for line in self._smoothed_lines[self._starting_acceleration_lines:]:
            # The chance starts at 20% for flat lines, and is increased or decreased by the angle, maxing at 100%
            # for angles of 36 degrees of more, and dropping to 0% chance at angles less than -25 degrees.
            chance = min(line.angle / 45 + settings.MINIMUM_ACCELERATION_CHANCE, 1)
            if random() < chance:
                line.type = LineType.ACCELERATION
            else:
                line.type = LineType.NORMAL


@dataclass
class Point:
    x: float
    y: float
    date_recorded: date = date.today()

    def rescale(self, x_scale, y_scale):
        return Point(
            x=self.x / x_scale,
            y=self.y / y_scale,
            date_recorded=self.date_recorded
        )


class LineType:
    NORMAL = 0
    ACCELERATION = 1
    SCENERY = 2


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
    type: int = LineType.NORMAL

    def __len__(self):
        return math.sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2)

    @property
    def gradient(self):
        delta_x = self.point_a.x - self.point_b.x
        delta_y = self.point_a.y - self.point_b.y

        return delta_y / delta_x

    @property
    def angle(self):
        """Returns the negative angle in degrees (as linerider inverts the y-axis)"""
        return -math.degrees(math.atan(self.gradient))

    @property
    def date_recorded(self) -> date:
        return self.point_a.date_recorded
