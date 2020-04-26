from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from export.export_to_json import track_to_json
from datetime import date
import settings


x_scale = float(input('How many days per unit of the x axis do you want? (default 0.1 days per x)') or 0.1)
y_scale = -float(input('How many $ per unit of the y axis do you want? (default 0.1 days per y)') or 0.1)

ticker = input("What ticker symbol do you want to track? (Default $SPY)") or "SPY"
start_date = input("What date would you like the track to start at? (Default - earliest available)") or '1900-01-01'
end_date = input("What date would you like the track to end at? (Default - latest available)") or str(date.today())

data = tiingo_client.get(start_date, end_date, ticker)
start = data[0]['close']
track = Track(
    parser.parse(start_date or '1900-01-01').date(),
    parser.parse(end_date or str(date.today())).date(),
    x_scale,
    y_scale,
    ticker,
    [
        Point(
            idx + settings.STARTING_AREA_X * x_scale,
            day['close'] - start + settings.STARTING_AREA_Y * y_scale,
            parser.parse(day['date']).date()
        )
        for idx, day in enumerate(data)
    ]
)
track_to_json(track)
