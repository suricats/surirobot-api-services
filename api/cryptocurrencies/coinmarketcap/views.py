import logging
import json
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException, MissingHeaderException, BadHeaderException, OperationFailedException, ResourceNotFoundException


crypto_cmc = Blueprint('crypto_cmc', __name__)
logger = logging.getLogger(__name__)


@crypto_cmc.route('/get', methods=['GET'])
def get():
    errors = []
    return "test"
