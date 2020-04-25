from models import Track, Line
from datetime import date

example_track = Track(start_date=date('2010-01-01'), end_date=date('2020-01-01'))
example_track.lines.add(
    Line(
        point_a=(-10, 20),
        point_b=(50, 25)
    )
)