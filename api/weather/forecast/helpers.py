import requests
import os
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException, ResourceNotFoundException, BadParameterException

with open(os.getcwd() + '/res/credentials/forecast.json', 'r') as file:
    FORECAST_CREDENTIALS = json.load(file)
token = FORECAST_CREDENTIALS['API_KEY']

def forecast_get_weather(source='google-news-fr'):
    res = requests.get('https://api.darksky.net/forecast/' + token + '/37.8267,-122.4233')
    print(res.content)
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 400:
        raise BadParameterException(source)
    else:
        raise ExternalAPIException(api_name='Google News', description='http_code:{}'.format(res.status_code))
