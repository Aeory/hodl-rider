from datetime import date
from tiingo import TiingoClient
import settings
from typing import Union, List
from utils.cache import json_cache

client = TiingoClient(settings.TIINGO_CONFIG)


@json_cache('tiingo_client')
def get(from_date: Union[str, None], to_date: Union[str, None], ticker: str = 'BTC') -> List[dict]:
    data = client.get_ticker_price(
        ticker=ticker,
        fmt='json',
        startDate=from_date,
        endDate=to_date or str(date.today()),
        frequency=settings.RESAMPLE_FREQUENCY
    )
    return data
