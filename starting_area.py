from models import Point, Line, LineType
import settings

starting_lines = [
    Line(
        point_a=Point(x=-5, y=settings.STARTING_AREA_Y),
        point_b=Point(x=settings.STARTING_AREA_X, y=settings.STARTING_AREA_Y),
        type=LineType.ACCELERATION,
    )
]
