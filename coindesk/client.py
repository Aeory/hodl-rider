import requests
from utils.cache import json_cache

COINDESK_API = "https://api.coindesk.com/v1/bpi/historical/close.json"


@json_cache("coindesk")
def get(from_date: str, to_date: str) -> dict:
    result = requests.get(COINDESK_API, params={"start": from_date, "end": to_date})

    result_json = result.json()

    return result_json["bpi"]
