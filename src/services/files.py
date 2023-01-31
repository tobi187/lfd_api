import base64
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os
import uuid


# BASE_PATH = r"C:\Users\fischert\Desktop\projects\home\lfd_api\temp"
# BASE_PATH = r"C:\Users\fisch\Desktop\projects\api\lfd_api\temp"
BASE_PATH = r"C:\Users\fisch\Desktop\projects\web\lfd_api\temp"
ALLOWED_EXTENSION = "docx"


def validate_file(file: FileStorage) -> str:
    if not file or not file.filename:
        return "-1"
    if file.filename.rsplit(".")[0].lower() != ALLOWED_EXTENSION:
        return "-1"
    if "." not in file.filename:  # type: ignore
        return "-1"

    file_name = secure_filename(file.filename)
    file.save(os.path.join(BASE_PATH, file_name))  # type: ignore
    return file_name


def store_file_very_unsecure(file):
    content = base64.b64decode(file)

    file_name = str(uuid.uuid4())

    path = os.path.join(BASE_PATH, file_name + ".docx")

    with open(path, "wb") as file:
        file.write(content)

    return file_name
