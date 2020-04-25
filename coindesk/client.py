import json
import requests
import os

COINDESK_API = 'https://api.coindesk.com/v1/bpi/historical/close.json'


def get(from_date: str, to_date: str) -> dict:
    cache_name = f'coindesk/cache/{from_date}-{to_date}.json'
    if os.path.exists(cache_name):
        return json.loads(open(cache_name).read())

    result = requests.get(
        COINDESK_API,
        params={
            'start': from_date,
            'end': to_date
        }
    )

    result_json = result.json()
    open(cache_name, 'w').write(json.dumps(result_json))

    return result_json['bpi']
