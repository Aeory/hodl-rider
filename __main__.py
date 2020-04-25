from coindesk import client
from models import Track, Point
from dateutil import parser
from utils.export_to_json import track_to_json


START_DATE = '2010-07-17'
END_DATE = '2020-04-25'

X_SCALE = 0.1
Y_SCALE = -10


index_data = client.get(START_DATE, END_DATE)

track = Track(
    parser.parse(START_DATE),
    parser.parse(END_DATE),
    X_SCALE,
    Y_SCALE,
    'BTC',
    [
        Point(
            i,
            v
        )
        for i, v in enumerate(index_data.values())
    ]
)

track_to_json(track)

