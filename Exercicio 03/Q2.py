from os import system

# C:\DSS-TESTE\Sophia.mp4
# C:\DSS-TESTE\Sophia.mp4 & cd C:\ & dir 
try:
	possible_characters = [' ', '/', '\\', ':', '-', '.', 
	'1', '2', '3', '4', '5', '6', '7', '8', '9',
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z',
	'á', 'ã', 'à', 'â', 'í', 'ì', 'î', 'ú', 'ù', 'û', 'é', 'è', 'ê', 'ó', 'ò', 'õ', 'ô']

	video_path = input("Informe o diretorio do video: ")
	for letter in video_path.lower():
		if letter not in possible_characters:
			raise Exception("Caractere \'" + letter + "\' não permitido.")

	system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + video_path)
 
except (Exception) as error:
  print ("Erro: ", error)