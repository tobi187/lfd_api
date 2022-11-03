import json

PATHS = {
    "systemIntegration": "data/systemintegration.json"
}


def try_find(name):
    if name not in PATHS.keys():
        return {"status": 404}

    with open(r"C:\Users\fischert\Desktop\projects\home\lfd_api\src\data\systemintegration.json", "r") as file:
        data = json.load(file)

    return {
        "status": 200,
        "data": data
    }


def all_jobs():
    jobs = [
        ("systemIntegration", "System Integration"),
        ("coder", "Anwendungsentwickler"),
        ("lager", "Lager Fachkraft")
    ]

    mapped_jobs = [{"display": d, "internal": v} for v, d in jobs]

    return mapped_jobs
