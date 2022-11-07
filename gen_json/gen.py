import json

part = input("Abschnitt: ").strip().upper()
number = input("Lfd Nr: ").strip()
summary = ""


def create_obj(k: str, v: str):
    return {
        "lfd": part + number + k,
        "text": v,
    }


def read_text():
    with open("input.txt", "r+", encoding="utf-8") as f:
        global summary
        arr, summary = f.read().split("\n\n")

        arr = arr.replace("\n", " ")
    nString = arr[0]
    for i in range(1, len(arr) - 5):
        if arr[i+1] == ")":
            nString += "~"
        nString += arr[i]

    nString += arr[-5:]

    data = [e.split(")") for e in nString.split("~")]
    return [create_obj(f.strip(), s.strip()) for f, s in data]


whatever = read_text()
result = {
    "ueberbegriff": summary.replace("\n", " ").strip(),
    "points": whatever
}

print(result)

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2, ensure_ascii=False)
