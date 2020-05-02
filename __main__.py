from tiingo_client import client as tiingo_client
from models import Track, Point
from dateutil import parser
from export.export_to_json import track_to_json, create_json
from datetime import date
import settings
from api import hodl

ticker = input("What ticker symbol do you want to track? (Default $SPY)") or "SPY"
start_date = (
    input(
        "What date would you like the track to start at? (Default - earliest available)"
    )
    or "1900-01-01"
)
end_date = input(
    "What date would you like the track to end at? (Default - latest available)"
) or str(date.today())

json_data = hodl(ticker, start_date, end_date)

create_json(json_content=json_data, filename=f"{ticker.upper()}-hodl-rider")
