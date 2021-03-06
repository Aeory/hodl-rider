import json

from models import Track
from export.models.track import LineRiderTrack


def track_to_json(track: Track):
    linerider_track = LineRiderTrack(track)
    content = json.dumps(linerider_track.to_json())
    return content


def create_json(filename: str = "example", json_content: str = "{}"):
    with open(f"tracks/{filename}.json", "w+") as file:
        file.write(json_content)
    return file.name
