import logging
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException, MissingHeaderException, BadHeaderException, OperationFailedException

weather_forecast = Blueprint('weather_forecast', __name__)
logger = logging.getLogger(__name__)


@weather_forecast.route('/text', methods=['POST'], defaults={'want': 'text'})
@weather_forecast.route('/audio', methods=['POST'],  defaults={'want': 'audio'})
def weather(want):
    errors = []
