import os
from zipfile import ZipFile
from RequestAtt import request_actualization

def unzip(file_name="Actualization.zip"):
    """
    Unzip a file

    params: 
     - file_name: name of the file to unzip 
    """
    with ZipFile(file_name, 'r') as zip:
        zip.extractall()  
 
print(request_actualization())
unzip()
os.system("python App.py") 
os.remove("Actualization.zip")
