import logging
import json
from flask import Blueprint, request, jsonify, Response

from api.exceptions import MissingParameterException, InvalidCredentialsException, \
    BadParameterException, ExternalAPIException, APIException, MissingHeaderException, BadHeaderException, OperationFailedException, ResourceNotFoundException

from .helpers import coinmarketcap_get_currency

crypto_cmc = Blueprint('crypto_cmc', __name__)
logger = logging.getLogger(__name__)


@crypto_cmc.route('/<crypto>', methods=['GET'])
def get(crypto):
    try:
        res = coinmarketcap_get_currency(crypto)
        print(res)
        return jsonify({"value": float(res[0]['price_eur']), "evolution": float(res[0]['percent_change_24h'])}), 200
    except (ExternalAPIException, ResourceNotFoundException) as e:
        return jsonify({'errors': [dict(e)]}), e.status_code
    except Exception as e:
        logger.error(e)
        return jsonify({'errors': [dict(APIException('crypto_parse_data'))]}), 500
