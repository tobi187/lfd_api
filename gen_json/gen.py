import json
import html

part = input("Abschnitt: ").strip()
number = input("Lfd Nr: ").strip()
summary = input("Überbegriff: ").strip()


def create_obj(k: str, v: str):
    return {
        "lfd": part + number + k,
        "text": v,
    }


def read_text():
    with open("input.txt", "r+") as f:
        arr = html.escape(f.read().replace("\n", ""))

    nString = arr[0]
    for i in range(1, len(arr) - 5):
        if arr[i+1] == ")":
            nString += "~"
        nString += arr[i]

    nString += arr[-5:]

    data = [e.split(")") for e in nString.split("~")]
    return [create_obj(e[0].strip(), e[1].strip()) for e in data]


result = {
    "ueberbegriff": summary.replace("\n", ""),
    "points": read_text()
}

with open("output.json", "w") as f:
    json.dump(result, f, indent=2)
