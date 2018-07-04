import logging
import random
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException, ResourceNotFoundException

from .helpers import google_news_get_news
news_google = Blueprint('news_google', __name__)
logger = logging.getLogger(__name__)


@news_google.route('/<source>', methods=['GET'])
@news_google.route('/', methods=['GET'],  defaults={'source': None})
def get(source):
    try:
        if source:
            res = google_news_get_news(source)
        else:
            res = google_news_get_news()
        index = random.randint(0, len(res['articles'])-1)
        message = res['articles'][index].get('title') + ' : ' + res['articles'][index].get('description')
        print(message)
        return jsonify({'message': message}), 200
    except (ExternalAPIException, BadParameterException) as e:
        return jsonify({'errors': [dict(e)]}), e.status_code
    except Exception as e:
        logger.error(e)
        return jsonify({'errors': [dict(APIException('news_parse_data({})'.format(type(e).__name__)))]}), 500
