from logging import getLogger
import json
from typing import List
from models import Line
from export.models.line import LineRiderLine


logger = getLogger(__name__)

def string_to_track(s: str, x: float, y: float, scale: float = 1.0, x_gap: float = 66.5):
    x_gap *= scale

    track = []
    for i, c in enumerate(s.upper()):
        if c == ' ':
            continue

        try:
            char_lines = json.loads(open(f'linewriter/chars/{c}.json').read())
        except FileNotFoundError:
            logger.warning(f"String writer could not find character '{c}'")

        for line in char_lines:
            line['x1'] *= scale
            line['x2'] *= scale
            line['y1'] *= scale
            line['y2'] *= scale

            line['x1'] += (i * x_gap) + x
            line['x2'] += (i * x_gap) + x
            line['y1'] += y
            line['y2'] += y

            track.append(LineRiderLine(line))

    return track
