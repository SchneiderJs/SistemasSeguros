import requests
url  = "http://127.0.0.1:5000/"
data = {'upload_file': open('server/Atualizacao','rb')}
params = {"name": "C:\\temp\Atualizacao.txt"}
resp = requests.post(url, data=data, params=params)

