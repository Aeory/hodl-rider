from coindesk import client as coindesk_client
from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from utils.export_to_json import track_to_json


START_DATE = None
END_DATE = '2020-04-25'

X_SCALE = 0.1
Y_SCALE = -0.1

TICKER = "SPY"

if TICKER == 'BTC':
    index_data = coindesk_client.get(START_DATE, END_DATE)

    track = Track(
        parser.parse(START_DATE or '1900-01-01'),
        parser.parse(END_DATE or '1900-01-01'),
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
        parser.parse(END_DATE or '1900-01-01'),
        X_SCALE,
        Y_SCALE,
        TICKER,
        [
            Point(
                idx,
                day['close'] - start - 3
            )
            for idx, day in enumerate(data)
        ]
    )
track_to_json(track)

