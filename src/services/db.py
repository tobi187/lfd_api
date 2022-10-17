import json

PATHS = {
    "systemIntegration": "data/systemintegration.json"
}


def try_find(name):
    if name not in PATHS.keys():
        return {"status": 404}

    with open(r"C:\Users\fisch\Desktop\projects\web\lfd_api\src\data\systemIntegration.json", "r") as file:
        data = json.load(file) 

    return {
        "status": 200,
        "data": data
    }
