import os
from zipfile import ZipFile
from RequestAtt import request_actualization 

def safe_unzip(file_name="Actualization.zip", password="password"):
    with ZipFile(file_name) as zip:
        if(zip.pwd != password):
            raise(Exception("Não foi possivel realizar a atualizacao"))
        zip.extractall(pwd=bytes(password, 'utf-8')) 

try:
    print(request_actualization())
    safe_unzip()
    os.system("python App.py")
except Exception as e:
    print(e) 
finally:
    os.remove("Actualization.zip")