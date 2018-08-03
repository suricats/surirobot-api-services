import logging
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException, MissingHeaderException, BadHeaderException, OperationFailedException

from .helpers import forecast_get_weather

weather_forecast = Blueprint('weather_forecast', __name__)
logger = logging.getLogger(__name__)


@weather_forecast.route('/', methods=['POST'])
def weather():
    errors = []

    if request.json:
        if 'latitude' not in request.json:
            errors.append(dict(MissingParameterException('latitude')))

        if 'longitude' not in request.json:
            errors.append(dict(MissingParameterException('longitude')))

        if 'time' not in request.json:
            errors.append(dict(MissingParameterException('time')))

        if 'language' not in request.json:
            errors.append(dict(MissingParameterException('language')))

        if errors:
            return jsonify({'errors': errors}), 400

        latitude = request.json['latitude']
        longitude = request.json['longitude']
        time = request.json['time']
        language = request.json['language']
        try:
            res = forecast_get_weather(latitude, longitude, time, language)
            output = {
                "currently": res["currently"],
                "daily": res["daily"]["data"][0],
                "timezone": res["timezone"]
            }
            return jsonify(output), 200
        except InvalidCredentialsException as e:
            return jsonify({'errors': [dict(e)]}), e.status_code
        except ExternalAPIException as e:
            return jsonify({'errors': [dict(e)]}), e.status_code
        except Exception as e:
            logger.error(e)
            return jsonify({'errors': [dict(APIException('weather_parse({})'.format(type(e).__name__)))]}), 500

    else:
        errors.append(dict(APIException('no_content')))
        return jsonify({'errors': errors}), 400
