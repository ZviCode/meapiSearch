import re
from meapi import Me
from flask import Flask, request

me = Me(phone_number="972++++++")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def parse_request():
    phone = request.args.get('phone', None)
    if not phone:
        return "error: phone is required", 400
    phone_number = re.findall(r'[\d]+', phone.replace('-', ''))
    if len(phone_number) != 1:
        return "error: phone is invalid", 400
    phone_fixed = re.sub("^0", "972", phone_number[0])
    return me.phone_search(phone_fixed)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
