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
            y_scale: float = 100,
            ticker: str = "BTC",
            points: List['Point'] = None,
            smoothing_coefficient: int = 5
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

        self._smoothing_algorithm = 'ROLLING_AVERAGE'

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
                last_n_points = self.points[i - (self._smoothing_coefficient-1): i+1]

                averaged_point = Point(
                    x=sum([point.x for point in last_n_points]) / self._smoothing_coefficient,
                    y=sum([point.y for point in last_n_points]) / self._smoothing_coefficient
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

        return self._smoothed_lines


@dataclass
class Point:
    x: float
    y: float

    def rescale(self, x_scale, y_scale):
        return Point(
            x=self.x / x_scale,
            y=self.y / y_scale
        )


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
        return math.sqrt((self.point_b.x - self.point_a.x) ** 2 + (self.point_b.y - self.point_a.y) ** 2)

    @property
    def gradient(self):
        delta_x = self.point_a.x - self.point_b.x
        delta_y = self.point_a.y - self.point_b.y

        return delta_y / delta_x
