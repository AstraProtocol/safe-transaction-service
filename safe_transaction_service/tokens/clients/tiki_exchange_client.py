import logging

import requests

from .exceptions import CannotGetPrice

logger = logging.getLogger(__name__)


class TikiExchangeClient:
    def __init__(self):
        self.http_session = requests.Session()

    def _get_price(self) -> float:
        url = f"https://api.tiki.vn/sandseel/api/v2/public/markets/astra/summary"
        try:
            response = self.http_session.get(url, timeout=10)
            api_json = response.json()
            if not response.ok:
                logger.warning("Cannot get price from url=%s", url)
                raise CannotGetPrice(api_json.get("msg"))

            price = float(api_json["ticker"]["last"])
            if not price:
                raise CannotGetPrice(f"Price from url={url} is {price}")
            return price
        except (ValueError, IOError) as e:
            raise CannotGetPrice from e

    def get_asa_usd_price(self) -> float:
        return self._get_price()
