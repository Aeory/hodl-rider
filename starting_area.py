from models import Point, Line, LineType
import settings

starting_lines = [
    Line(
        point_a=Point(x=-5, y=1),
        point_b=Point(x=settings.STARTING_AREA_X, y=1),
        type=LineType.ACCELERATION
    )
]
