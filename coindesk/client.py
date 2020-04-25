import requests

COINDESK_API = 'https://api.coindesk.com/v1/bpi/historical/close.json'


def get(from_date: str, to_date: str) -> dict:
    return requests.get(
        COINDESK_API,
        params={
            'from_date': from_date,
            'to_date': to_date
        }
    ).json()['bpi']

