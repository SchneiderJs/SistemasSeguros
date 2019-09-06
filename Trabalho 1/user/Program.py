import os
import requests
from zipfile import ZipFile

def request_actualization():
    url  = "http://127.0.0.1:5000/"
    files = {'file': open('../server_data/Atualizacao.zip', 'rb')}
    
    new_file_with_path = os.getcwd() + "/Atualizacao.zip"
    json = {"name": new_file_with_path}

    return requests.post(url, files=files, data=json) 


def unzip(file_name = "Atualizacao.zip"):
    with ZipFile(file_name, 'r') as zip:
        zip.extractall()
    os.remove(file_name)

print(request_actualization())
unzip()
