import os
import requests
def request_actualization():
    url  = "http://127.0.0.1:5000/"
    files = {'file': open('../server_data/Actualization.zip', 'rb')}
    
    new_file_with_path = os.getcwd() + "/Actualization.zip"
    json = {"name": new_file_with_path}

    return requests.post(url, files=files, data=json) 
