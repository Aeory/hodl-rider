from datetime import date
from tiingo import TiingoClient
from tiingo.restclient import RestClientError

import settings
from typing import Optional, List
from utils.cache import json_cache
import json

from utils.exceptions import ValidationException

client = TiingoClient(settings.TIINGO_CONFIG)


@json_cache("tiingo_client")
def _cached_get(
    ticker: str
) -> List[dict]:
    try:
        data = client.get_ticker_price(
            ticker=ticker,
            fmt="json",
            frequency=settings.RESAMPLE_FREQUENCY,
            startDate=str(date.fromtimestamp(0)),
            endDate=str(date.today())
        )
        return data
    except RestClientError as e:
        response = e.args[0].response
        if response.headers['Content-Type'] == 'application/json':
            json_body = json.loads(response.text)
            if 'not found' in (details := json_body['detail']):
                raise ValidationException(
                    message=details
                ) from e
            else:
                raise


def get(
    from_date: Optional[str], to_date: Optional[str], ticker: str = "BTC"
) -> List[dict]:
    start_date = from_date
    end_date = to_date or str(date.today())

    ticker_data = _cached_get(
        ticker=ticker
    )

    return [
        data_point for data_point in ticker_data
        if start_date <= data_point['date'] <= end_date
    ]
