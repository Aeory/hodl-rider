from coindesk import client as coindesk_client
from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from utils.export_to_json import track_to_json
from datetime import date

X_SCALE = float(input('How many days per unit of the x axis do you want? (default 0.1 days per x)') or 0.1)
Y_SCALE = -float(input('How many $ per unit of the y axis do you want? (default 0.1 days per y)') or 0.1)

TICKER = input("What ticker symbol do you want to track? (Default $SPY)") or "SPY"
START_DATE = input("What date would you like the track to start at? (Default - earliest available)") or '1900-01-01'
END_DATE = input("What date would you like the track to end at? (Default - latest available)") or str(date.today())

if TICKER == 'BTC':
    index_data = coindesk_client.get(START_DATE, END_DATE)

    track = Track(
        parser.parse(START_DATE),
        parser.parse(END_DATE),
        X_SCALE,
        Y_SCALE,
        TICKER,
        [
            Point(
                i,
                v
            )
            for i, v in enumerate(index_data.values())
        ]
    )
else:
    data = tiingo_client.get(START_DATE, END_DATE, TICKER)
    start = data[0]['close']
    track = Track(
        parser.parse(START_DATE or '1900-01-01'),
        parser.parse(END_DATE or str(date.today())),
        X_SCALE,
        Y_SCALE,
        TICKER,
        [
            Point(
                idx - 2,
                day['close'] - start - 3
            )
            for idx, day in enumerate(data)
        ]
    )
track_to_json(track)
