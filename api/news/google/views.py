import logging
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException

news_google = Blueprint('news_google', __name__)
logger = logging.getLogger(__name__)


@news_google.route('/post', methods=['get'])
def post():
    errors = []
