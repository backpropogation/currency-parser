import xml.etree.ElementTree as ET

import requests
from constance import config

from apps.parser.models import Currency


def _parse_currencies():
    response = requests.get(config.CBR)
    currencies = ET.fromstring(response.content)
    Currency.objects.bulk_create(
        [
            Currency(
                name=currency[3].text,
                rate=float(currency[4].text.replace(',', '.'))/int(currency[2].text)
            )
            for currency in currencies
        ]
    )
