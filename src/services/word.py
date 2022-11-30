import os
import docx2txt
import docxtpl

BASE_PATH = r"C:\Users\fischert\Desktop\projects\home\lfd_api\temp"
# BASE_PATH = r"C:\Users\fisch\Desktop\projects\api\lfd_api\temp"


def extract_data(file_name: str) -> list[object]:
    start = False
    content: list[str] = []
    text: str = docx2txt.process(os.path.join(
        BASE_PATH, file_name + ".docx"))  # type: ignore
    lines = text.split("\n")

    for line in lines:
        if not start and line == "Ausbilder/in":
            start = True
        elif start and line.strip() == "{{ fill }}":
            points = [c for c in content if c != ""]
            return [{"index": i, "value": p, "lfd": ""} for i, p in enumerate(points)]
        elif start:
            content.append(line.strip())

    return []


def fill_file(content: list[object], file_name: str) -> None:
    docName = file_name + ".docx"
    doc = docxtpl.DocxTemplate(os.path.join(
        BASE_PATH, docName))  # type: ignore

    data = sorted(content, key=lambda x: x["index"])

    filler = {
        "fill": "\n".join([k["lfd"] for k in data])
    }

    doc.render(filler)  # type: ignore
    doc.save(os.path.join(BASE_PATH, docName))  # type: ignore
