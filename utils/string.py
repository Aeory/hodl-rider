import json


def string_to_track(s: str, x: float, y: float, scale: float = 1.0, x_gap: float = 66.5):
    x_gap *= scale

    track = []
    for i, c in enumerate(s.upper()):
        if c == ' ':
            continue

        char_lines = json.loads(open(f'chars/{c}.json').read())

        for line in char_lines:
            line['x1'] *= scale
            line['x2'] *= scale
            line['y1'] *= scale
            line['y2'] *= scale

            line['x1'] += (i * x_gap) + x
            line['x2'] += (i * x_gap) + x
            line['y1'] += y
            line['y2'] += y

            track.append(line)

    return track
