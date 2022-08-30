import re
from meapi import Me
from meapi.utils.validations import validate_phone_number, validate_uuid
from meapi.utils.exceptions import MeException, MeApiException
from flask import Flask, request
from flask import request
from logging import getLogger

_logger = getLogger(__name__)

me = Me(phone_number="972123456789") # Enter your phone number

app = Flask(__name__)

@app.route('/')
def a():
    return str(dict(request.args))

@app.route('/phone', methods=['GET'])
def phone_search():
    phone = request.args.get('p')
    if not phone:
        return {"err": "Phone must be provided"}, 500
    try:
        validate_phone_number(phone)
    except MeException:
        return {"err": "Not a valid phone number!"}, 500
    try:
        res = me.phone_search(re.sub( "^0", "972", phone))
        if res:
            _logger.info(f"Getting info on {phone}: {res.name}")
            return res.as_dict(), 200
        return {"err": "Not found"}, 404
    except MeApiException as e:
        _logger.error("ERROR: " + e.msg)
        return {"err": "unknown error"}, 500
    


@app.route('/profile/', methods=['GET'])
def parse_request():
    uuid = request.args.get('uuid')
    try:
        validate_uuid(uuid)
    except MeException:
        return {"err": "Not a valid UUID!"}, 500
    
    try:
        res = me.get_profile(uuid)
        _logger.info(f"Getting info on {uuid}: {res.name}")
        return res.as_dict(), 200
    except MeApiException as e:
        _logger.error("ERROR: " + e.msg)
        return {"err": "unknown error"}, 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
