import requests

url  = "http://127.0.0.1:5000/"
files = {'file': open('../server_data/Atualizacao', 'rb')}

json = {"name": "C:/Users/Schneider/Documents/Estudos/Universidade/FURB/Fase_6/DST/SistemasSeguros/Trabalho 1/user/Atualizacao.txt"}
response = requests.post(url, files=files, data=json) 

print(response)
