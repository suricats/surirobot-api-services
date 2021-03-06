import requests
import os
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException, ResourceNotFoundException, BadParameterException

with open(os.getcwd() + '/res/credentials/google.json', 'r') as file:
    GOOGLE_NEWS_CREDENTIALS = json.load(file)
token = GOOGLE_NEWS_CREDENTIALS['API_KEY']

def google_news_get_news(source='google-news-fr'):
    res = requests.get('https://newsapi.org/v2/top-headlines', params={'sources': source, 'apiKey': token})
    print(res.content)
    if res.status_code == 200:
        return res.json()
    elif res.status_code == 400:
        raise BadParameterException(source)
    else:
        raise ExternalAPIException(api_name='Google News', description='http_code:{}'.format(res.status_code))
