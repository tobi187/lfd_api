from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import os

BASE_ROUTE = ""
ALLOWED_EXTENSION = "docx"


def validate_file(file: FileStorage) -> str:
    if not file or not file.filename:
        return "-1"
    if  file.filename.rsplit(".")[0].lower() != ALLOWED_EXTENSION: 
        return "-1"      
    if "." not in file.filename:  # type: ignore
        return "-1"
    
    file_name = secure_filename(file.filename)
    file.save(os.path.join(BASE_ROUTE, file_name)) # type: ignore
    return file_name