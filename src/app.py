import os
from services.files import validate_file, store_file_very_unsecure
from services.db import try_find, all_jobs
from flask import Flask, jsonify, request, send_file
from flask_cors import CORS
from services.word import extract_data, fill_file


app = Flask(__name__)
CORS(app)

BASE_ROUTE = "/api/v1/"
BASE_PATH = r"C:\Users\fischert\Desktop\projects\home\lfd_api\temp"


@app.route(BASE_ROUTE + "/test", methods=["POST"])
def test():
    if request.method == "POST":
        file = request.files['file']
        print(request.form)
        file_name = validate_file(file)
        if file_name == "-1":
            return jsonify({"status": 400, "message": "Could not read or safe file"})

    return jsonify({"status": 400, "message": "only POST allowed"})


@app.route(BASE_ROUTE + "init")
def get_jobs():
    jobs = all_jobs()
    return {"status": 200, "jobs": jobs}


@app.route(BASE_ROUTE + "upload", methods=["POST"])
def save_file():
    if request.method == "POST":
        data = request.get_json()
        f_name = store_file_very_unsecure(data["wordData"])

        return {"status": 200, "name": f_name}
    return jsonify({"status": 400, "message": "only POST allowed"})


@app.route(f"{BASE_ROUTE}get-info", methods=["POST"])
def get_context():
    if request.method == "POST":
        req_data = request.get_json()
        points = extract_data(req_data["name"])

        if len(points) < 1:
            return jsonify({"status": 400, "message": "{{ fill }} not found"})

        job_data = try_find(req_data["job"])
        if job_data["status"] != 200:
            return jsonify({"status": 400, "message": "job not found"})

        return jsonify({"status": 200, "name": "dont know yet", "points": points, "data": job_data["data"]})

    return {"status": 400, "message": "only POST allowed"}


@app.route(BASE_ROUTE + "fill", methods=["POST"])  # type: ignore
def prepare_download():
    data = request.get_json()
    f_name = data["fileName"]
    lfd_data = data["data"]
    fill_file(lfd_data, f_name)

    return {"status": 200, "name": f_name}


@app.route(BASE_ROUTE + "dl/<name>")
def download_file(name):

    return send_file(os.path.join(BASE_PATH, name + ".docx"), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
