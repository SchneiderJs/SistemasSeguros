from os import system

video_path = input("Informe o diretorio do video: ")
print(video_path) # C:\DSS-TESTE\Sophia.mp4

# C:\DSS-TESTE\Sophia.mp4 & cd C:\ & dir
system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + video_path)


# C:\DSS-TESTE\Sophia.mp4 & cd C:\DSS-TESTE & dir
system("cd C:\Program Files\VideoLAN\VLC & vlc.exe " + video_path)

