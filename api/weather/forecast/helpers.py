import requests
import os
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException, ResourceNotFoundException, BadParameterException

with open(os.getcwd() + '/res/credentials/forecast.json', 'r') as file:
    FORECAST_CREDENTIALS = json.load(file)
token = FORECAST_CREDENTIALS['API_KEY']

def forecast_get_weather(lat, long, time, language):
    params = {'lang': language, 'units': 'auto'}
    res = requests.get('https://api.darksky.net/forecast/' + token + '/' + str(lat) + ',' + str(long) + ',' + str(time), params=params)
    print(res.content)
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 400:
        raise ExternalAPIException(api_name='Dark Sky', description=res.json())
    elif res.status_code == 401:
        raise InvalidCredentialsException('Dark Sky')
    else:
        raise ExternalAPIException(api_name='Dark Sky', description='http_code:{}'.format(res.status_code))
