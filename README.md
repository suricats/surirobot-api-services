# API Services

[![PyPI - Python Version](https://img.shields.io/badge/python-3.6-blue.svg)](https://docs.python.org/3/whatsnew/3.6.html)

This API provides all the necessary endpoints to give access to specific informations to Surirobot.

## Features

* Weather
  * Forecast

* News
  * Google News

* Cryptocurrencies
  * CoinMarkerCap
  
## Requirements
* Python3 
* Virtualenvwrapper ```pip install virtualenvwrapper```
* If you have some trouble with the command ```workon``` see : https://stackoverflow.com/questions/29900090/virtualenv-workon-doesnt-work

## Installation

* Clone repository
* Create virtualenv
```shell
mkvirtualenv suri-api-services && workon suri-api-services
```

* Install dependencies
```shell
pip install -r requirements.txt
```

* If you wants to run the test suite:
```shell
pip install -r requirements-dev.txt
```


* Configure .env
```shell
cp .env.example .env
```

* Option 1 - Drop your Google API credentials in res/credentials folder
  * forecast.json - Forecast
  * google.json - Google News
  * coinmarketcap.json - CoinMarkerCap

* Option 2 (suri-downloader) -  Fill the login & password fields in env and do:
```shell
# Use export commands only if those inputs are not fulfilled in .env file
export $REMOTE_DATA_LOGIN=<value>
export $REMOTE_DATA_PASSWD=<value>
tools/get-credentials
```

* Run the dev server
```shell
./app.py
```

* Run the production server
```shell
gunicorn -w 4 -b 127.0.0.1:5000 wsgi:app
```

## Docs

The Openapi spec and a postman collection are available in the `doc` folder.
You can render the documentation by pointing your browser at the url given by the server.
