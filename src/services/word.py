import os
import docx2txt
import docxtpl

BASE_PATH = ""

def extract_data(file_name: str) -> list[str]:
    start = False
    content: list[str] = []
    text: str = docx2txt.process(os.path.join(BASE_PATH, file_name)) # type: ignore
    lines = text.split("\n")

    for line in lines:
        if not start and line == "Ausbilder/in":
            start = True
        if start and line.strip() == "{{ fill }}":
            return [c for c in content if c != ""]
        elif start:
            content.append(line.strip())

    return []


def fill_file(content: dict[int, int], file_name: str) -> None:
    doc = docxtpl.DocxTemplate(os.path.join(BASE_PATH, file_name)) # type: ignore
    data = dict(sorted(content.items()))
    filler = {
        "fill": "\n".join([str(data[k]) for k in data])
    }

    doc.render(filler) # type: ignore
    doc.save(os.path.join(BASE_PATH, file_name)) # type: ignore