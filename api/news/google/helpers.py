import requests
import os
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException

with open(os.getcwd() + '/res/credentials/google.json', 'r') as file:
    GOOGLE_NEWS_CREDENTIALS = json.load(file)
