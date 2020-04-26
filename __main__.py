from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from utils.export_to_json import track_to_json
from datetime import date

TICKER = input("What ticker symbol do you want to track? (Default $SPY)") or "SPY"
START_DATE = input("What date would you like the track to start at? (Default - earliest available)") or '1900-01-01'
END_DATE = input("What date would you like the track to end at? (Default - latest available)") or str(date.today())


SCALES = {
    'btcusd': (0.1, -10)
}

X_SCALE, Y_SCALE = SCALES.get(TICKER, (0.1, 0.1))

print(f'Scales X:{X_SCALE} Y:{Y_SCALE}')

data = tiingo_client.get(START_DATE, END_DATE, TICKER)
start = data[0]['close']
track = Track(
    parser.parse(START_DATE),
    parser.parse(END_DATE),
    X_SCALE,
    Y_SCALE,
    TICKER,
    [
        Point(
            idx - 2,
            day['close'] - start - 3,
            parser.parse(day['date']).date()
        )
        for idx, day in enumerate(data)
    ]
)

track_to_json(track)
