from flask import Flask , request
from flask_cors import CORS
import os
# from src.controller.testing import testing as debugger

set_port = os.getenv("PORT")
app = Flask(__name__) 
CORS(app)


@app.route("/debug", methods = ['GET'])
def testing():
    if(request.method == 'GET'):
        return "OK"
        # debugger()

if __name__ == '__main__':
    app.run(port=3422)

