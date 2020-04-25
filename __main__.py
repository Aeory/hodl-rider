from coindesk import client
from models import Track, Line
from dateutil import parser


START_DATE = '2010-01-01'
END_DATE = '2020-04-25'

X_SCALE = 1
Y_SCALE = 1


index_data = client.get(START_DATE, END_DATE)

track = Track(
    parser.parse(START_DATE),
    parser.parse(END_DATE),
    X_SCALE,
    Y_SCALE,
    [
        Line(

        )
    ]
)
