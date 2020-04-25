from models import Track, Line
import json
import datetime


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
    for idx, line in enumerate(track.smoothed_lines):
        linerider_line = {
            "id": idx + 1,
            "type": int(not idx % 2),
            "x1": line.point_a.x,
            "y1": line.point_a.y,
            "x2": line.point_b.x,
            "y2": line.point_b.y,
            "flipped": False,
            "leftExtended": False,
            "rightExtended": False
        }
        linerider_track['lines'].append(linerider_line)

    last_index = idx
    for idx, line in enumerate(track.lines):
        linerider_line = {
            "id": idx + 1 + last_index,
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
    content = json.dumps(linerider_track)
    create_json(filename=linerider_track['label'], json_content=content)
    return linerider_track


def create_json(filename: str="example", json_content: str= "{}"):
    with open(f"{filename}.json", 'w+') as file:
        file.write(json_content)
    return file.name
