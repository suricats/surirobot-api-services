from flask import Flask, redirect, Response
from flask_swagger_ui import get_swaggerui_blueprint
from api.cryptocurrencies.coinmarketcap.views import crypto_cmc
from api.news.google.views import news_google
from api.weather.forecast.views import weather_forecast

app = Flask(__name__)

app.register_blueprint(crypto_cmc, url_prefix='/api/crypto')
app.register_blueprint(news_google, url_prefix='/api/news')
app.register_blueprint(weather_forecast, url_prefix='/api/weather')
app.register_blueprint(get_swaggerui_blueprint('/docs', '/docs/openapi.yaml'), url_prefix='/docs')


@app.route('/')
def index():
    return redirect('/docs', code=301)


@app.route('/docs/openapi.yaml')
def swagger_file():
    content = open('./docs/openapi.yaml', 'r')
    return Response(content, mimetype="text/yaml")
