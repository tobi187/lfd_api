from services.files import validate_file
from services.db import try_find
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_ROUTE = "/api/v1/"


@app.route(BASE_ROUTE + "/test", methods=["POST"])
def test():
    if request.method == "POST":
        file = request.files['file']
        file_name = validate_file(file)
        if file_name == "-1":
            return jsonify({"status": 400, "message": "Could not read or safe file"})

    return jsonify({"status": 400, "message": "only POST allowed"})


@app.route(BASE_ROUTE + "init", methods=["POST"])
def get_data():
    if request.method == "POST":
        rdata = request.get_json()

        result = rdata["job"]
        response = jsonify(try_find(result))

        #response.headers.add('Access-Control-Allow-Origin', '*')
        #response.headers.add("Access-Control-Allow-Methods", "POST")
        return response

    return {"status": 400, "message": "only POST allowed"}


if __name__ == "__main__":
    app.run(debug=True)
