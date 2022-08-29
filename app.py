import re
from meapi import Me
from flask import Flask, request
from flask import request

me = Me(phone_number="972++++++")

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def parse_request():
    try:
        phone = request.args.getlist('phone')
        me_search  = me.phone_search( re.sub( "^0" , "972" , phone[0] ) )
        try:
            print (me_search)
            return me_search
        except:
            return "error request me"
    except:
        return "error global , I get the value phone"
    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=12345)
