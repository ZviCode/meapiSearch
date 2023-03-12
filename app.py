import json
import http.client
import re
from meapi import Me
from flask import Flask, request

me = Me(phone_number="972********")

app = Flask(__name__)

def get_nikud(text: str) -> str:
    conn = http.client.HTTPSConnection("nakdan-5-1.loadbalancer.dicta.org.il")
    payload = json.dumps({
        "data": text,
        "genre": "modern"
    })
    headers = {
        'Content-Type': 'application/json'
    }
    conn.request("POST", "/api", payload, headers)
    res = conn.getresponse()
    data = json.loads(res.read().decode("utf-8"))
    words = map(lambda w: w['options'][0] if len(w['options']) > 0 else w['word'], data)
    return "".join(words)


@app.route('/', methods=['GET', 'POST'])
def parse_request():
    phone = request.args.get('phone', None)
    if not phone:
        return "error: phone is required", 400
    phone_number = re.findall(r'[\d]+', phone.replace('-', ''))
    if len(phone_number) != 1:
        return "error: phone is invalid", 400
    phone_fixed = re.sub("^0", "972", phone_number[0])
    me_search_result = me.phone_search(phone_fixed)
    nikud = request.args.get('nikud', False)
    if not nikud:
        print(me_search_result)
        return me_search_result.as_dict()
   
    else:
        name = me_search_result['contact'].get('name')
        menukad_name = get_nikud(name)
        return {
            **me_search_result,
            'menukad_name': menukad_name
        }


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
