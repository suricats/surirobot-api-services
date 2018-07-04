import os
import requests
import json

from api.exceptions import ExternalAPIException, InvalidCredentialsException, OperationFailedException, ResourceNotFoundException

with open(os.getcwd() + '/res/credentials/coinmarketcap.json', 'r') as file:
    CMC_CREDENTIALS = json.load(file)

token = CMC_CREDENTIALS['token']
headers = {'Authorization': 'Token ' + token, 'Content-Type': 'application/json'}
