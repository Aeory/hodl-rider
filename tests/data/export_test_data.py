from models import Track, Line, Point
from dateutil import parser

example_track = Track(start_date=parser.parse('2010-01-01'), end_date=parser.parse('2020-01-01'))
example_track.lines.append(
    Line(
        point_a=Point(x=-10, y=20),
        point_b=Point(x=50, y=25)
    )
)