from models import Track, Line
import json
import datetime

from utils.string import string_to_track


def track_to_json(track: Track, filename=None):
    linerider_track = {
        "label": filename or f"{track.ticker}-hodl-rider",
        "creator": "hodl-rider v0.1",
        "description": "",  # f"Line rider created with hodl-rider tracking {track.ticker} from {track.from_date} to {track.to_date}.",
        "duration": 40,
        "version": "6.2",
        "audio": None,
        "startPosition": {
            "x": 0,
            "y": 0
        },
        "riders": [
            {
                "startPosition": {
                    "x": 0,
                    "y": 0
                },
                "startVelocity": {
                    "x": 0.4,
                    "y": 0
                },
                "remountable": True
            }
        ],
        "layers": [
            {
                "id": 0,
                "name": "Base Layer",
                "visible": True
            }
        ],
        "lines": []
    }

    last_year = 0
    last_month = 0

    for idx, line in enumerate(track.smoothed_lines):

        linerider_line = {
            "type": line.type,
            "x1": line.point_a.x,
            "y1": line.point_a.y,
            "x2": line.point_b.x,
            "y2": line.point_b.y,
            "flipped": False,
            "leftExtended": False,
            "rightExtended": False
        }
        linerider_track['lines'].append(linerider_line)

        if (last_year < line.date_recorded.year) or (last_month < line.date_recorded.month):
            label = string_to_track(
                s=line.date_recorded.isoformat(),
                x=line.point_a.x,
                y=line.point_b.y - 50,
                scale=0.1
            )

            linerider_track['lines'].extend(label)

            last_year = line.date_recorded.year
            last_month = line.date_recorded.month

    for idx, line in enumerate(track.lines):
        linerider_line = {
            "type": 2,
            "x1": line.point_a.x,
            "y1": line.point_a.y,
            "x2": line.point_b.x,
            "y2": line.point_b.y,
            "flipped": False,
            "leftExtended": False,
            "rightExtended": False
        }
        linerider_track['lines'].append(linerider_line)

    for i, line in enumerate(linerider_track['lines']):
        line['id'] = i

    content = json.dumps(linerider_track)
    create_json(filename=linerider_track['label'], json_content=content)
    return linerider_track


def create_json(filename: str="example", json_content: str= "{}"):
    with open(f"tracks/{filename}.json", 'w+') as file:
        file.write(json_content)
    return file.name
