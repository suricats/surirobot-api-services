import os
import requests
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException, OperationFailedException, ResourceNotFoundException

def coinmarketcap_get_currency(currency, device='EUR'):
    print(currency)
    res = requests.get('https://api.coinmarketcap.com/v1/ticker/'+currency+'/?convert=EUR', params={'convert': device})
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 404:
        raise ResourceNotFoundException(currency)
    else:
        raise ExternalAPIException(api_name='CoinMarketCap', description='http_code:{}'.format(res.status_code))
