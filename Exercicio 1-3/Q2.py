# C:\DSS-TESTE\musica.mp3
# C:\DSS-TESTE\musica.mp3 & cd C:\ & dir 

from os import system

try:
	possible_characters = [' ', '/', '\\', ':', '-', '.', 
	'1', '2', '3', '4', '5', '6', '7', '8', '9',
	'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'z',
	'á', 'ã', 'à', 'â', 'í', 'ì', 'î', 'ú', 'ù', 'û', 'é', 'è', 'ê', 'ó', 'ò', 'õ', 'ô']

	music_path = input("Informe o diretório da música: ")
	for letter in music_path.lower():
		if letter not in possible_characters:
			raise Exception("Caractere \'" + letter + "\' não permitido.")

	system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + music_path)
 
except (Exception) as error:
  print ("Erro: ", error)