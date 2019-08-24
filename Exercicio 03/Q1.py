from os import system

# C:\DSS-TESTE\Sophia.mp4
# C:\DSS-TESTE\Sophia.mp4 & cd C:\ & dir 
video_path = input("Informe o diretorio da musica: ")
system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + video_path)