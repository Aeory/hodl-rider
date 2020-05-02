from typing import Union

from models import Line


class LineRiderLine:
    def __init__(self, line: Union[Line, dict]):
        if isinstance(line, Line):
            self.type = line.type
            self.x1 = line.point_a.x
            self.y1 = line.point_a.y
            self.x2 = line.point_b.x
            self.y2 = line.point_b.y
            self.flipped = False
            self.leftExtended = False
            self.rightExtended = False
        elif isinstance(line, dict):
            self.type = line["type"]
            self.x1 = line["x1"]
            self.y1 = line["y1"]
            self.x2 = line["x2"]
            self.y2 = line["y2"]
            self.flipped = line.get("flipped", False)
            self.leftExtended = line.get("leftExtended", False)
            self.rightExtended = line.get("rightExtended", False)
        else:
            raise NotImplementedError()
