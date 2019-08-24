# C:\DSS-TESTE\musica.mp3
# C:\DSS-TESTE\musica.mp3 & cd C:\ & dir 

from os import system

music_path = input("Informe o diretório da música: ")
system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + music_path)