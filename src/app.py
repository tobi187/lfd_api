from services.files import validate_file 
from flask import Flask, jsonify, request

app = Flask(__name__)

BASE_ROUTE = "/api/v1/"


@app.route("/test", methods=["POST"])
def test():
    if request.method == "POST":
        file = request.files['file']
        file_name = validate_file(file)
        if file_name == "-1":
            return jsonify({"status": 400, "message": "Could not read or safe file"})
        
         
    return jsonify({"status": 400, "message": "only POST allowed"})


if __name__ == "__main__":
    app.run(debug=True)

