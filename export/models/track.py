import json
from datetime import date, timedelta

from models import Track
from linewriter.string import string_to_track
import settings
from starting_area import starting_lines
from export.models.line import LineRiderLine


class LineRiderTrack:

    def __init__(self, track: Track):
        self.label = f"{track.ticker}-hodl-rider"
        self.creator = "hodl-rider v0.1"
        self.description = f"Line rider created with hodl-rider tracking {track.ticker} from {track.start_date} to {track.end_date}."
        self.version = "6.2"
        self.startPosition = {
            "x": 0,
            "y": -1
        }
        self.riders = [
            {
                "startPosition": {
                    "x": 0,
                    "y": 0
                },
                "startVelocity": {
                    "x": 0.2,
                    "y": 0
                },
                "remountable": True
            }
        ]
        self.lines = []

        time_covered = track.end_date - track.start_date
        label_period = 'QUARTERS' if time_covered.days >= 365 else 'MONTHS'

        last_label_date = None
        for line in track.lines:
            self.lines.append(LineRiderLine(line))

            if (last_label_date is None) or \
               (label_period == 'QUARTERS' and self.date_to_quarter(last_label_date) != self.date_to_quarter(line.start_date)) or \
               (label_period == 'MONTHS' and last_label_date.month < line.start_date.month):

                if label_period == 'QUARTERS':
                    date_label = f'Q{self.date_to_quarter(line.start_date) + 1} {line.start_date.year}'
                else:
                    date_label = f'{line.start_date.isoformat()}'

                label = string_to_track(
                    s=f'{date_label} - ${line.price:.2f}',
                    x=line.point_a.x,
                    y=line.point_b.y - 50,
                    scale=0.1
                )
                self.lines.extend(label)
                last_label_date = line.start_date

        for line in track.smoothed_lines:
            self.lines.append(LineRiderLine(line))

        if settings.TITLE:
            self.lines.extend(
                string_to_track(f"${track.ticker}", 0, -200, scale=0.5)
            )
            self.lines.extend(
                string_to_track(f"{track.start_date} TO {track.end_date}", 300, -200, scale=0.2)
            )
        if settings.CREDITS:
            self.load_credits()
        if settings.STARTING_TRACK:
            self.create_starting_track()

        for idx, line in enumerate(self.lines):
            line.id = idx + 1

    def load_credits(self, scale: float = 1.0):
        credits_lines = json.loads(open(f'linewriter/credits.json').read())

        for line in credits_lines:
            line['x1'] *= scale
            line['x2'] *= scale
            line['y1'] *= scale
            line['y2'] *= scale

            self.lines.append(LineRiderLine(line))

    def create_starting_track(self):
        self.lines.extend([LineRiderLine(line) for line in starting_lines])

    def to_json(self):
        result = self.__dict__
        result['lines'] = [line.__dict__ for line in self.lines]
        return result

    @staticmethod
    def date_to_quarter(d: date) -> int:
        return (d.month - 1) // 3

