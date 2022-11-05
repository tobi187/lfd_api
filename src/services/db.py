import json
import os

PATHS = {
    "systemIntegration": "data/systemintegration.json"
}

BASE_PATH = r"C:\Users\fisch\Desktop\projects\api\lfd_api\src"
# BASE_PATH = r"C:\Users\fischert\Desktop\projects\home\lfd_api\src"


def try_find(name):
    if name not in PATHS.keys():
        return {"status": 404}

    with open(os.path.join(BASE_PATH, PATHS[name]), "r") as file:
        data = json.load(file)

    return {
        "status": 200,
        "data": data
    }


def all_jobs():
    jobs = [
        ("systemIntegration", "System Integration"),
        ("coder", "Gottgleiche Wesen"),
        ("lager", "Lager Fachkraft")
    ]

    mapped_jobs = [{"display": d, "internal": v} for v, d in jobs]

    return mapped_jobs
