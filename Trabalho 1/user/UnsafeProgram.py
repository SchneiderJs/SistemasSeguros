import os
from zipfile import ZipFile
from RequestAtt import request_actualization

def unzip(file_name="Atualizacao.zip"):
    with ZipFile(file_name, 'r') as zip:
        zip.extractall()  
 
print(request_actualization())
unzip()
os.system("python App.py") 
os.remove("Atualizacao.zip")
