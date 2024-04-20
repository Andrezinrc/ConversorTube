from pytube import YouTube
from pydub import AudioSegment
from colorama import Fore
import threading

def imprimir_banner():
    print(Fore.RED + " ██▓███ ▓██   ██▓▄▄▄█████▓ █    ██  ▄▄▄▄   ▓█████ ")
    print(Fore.RED + "▓██░  ██▒▒██  ██▒▓  ██▒ ▓▒ ██  ▓██▒▓█████▄ ▓█   ▀ ")
    print(Fore.RED + "▓██░ ██▓▒ ▒██ ██░▒ ▓██░ ▒░▓██  ▒██░▒██▒ ▄██▒███   ")
    print(Fore.RED + "▒██▄█▓▒ ▒ ░ ▐██▓░░ ▓██▓ ░ ▓▓█  ░██░▒██░█▀  ▒▓█  ▄ ")
    print(Fore.RED + "▒██▒ ░  ░ ░ ██▒▓░  ▒██▒ ░ ▒▒█████▓ ░▓█  ▀█▓░▒████▒")
    print(Fore.RED + "▒▓▒░ ░  ░  ██▒▒▒   ▒ ░░   ░▒▓▒ ▒ ▒ ░▒▓███▀▒░░ ▒░ ░")
    print(Fore.RED + "░▒ ░     ▓██ ░▒░     ░    ░░▒░ ░ ░ ▒░▒   ░  ░ ░  ░")
    print(Fore.RED + "░░       ▒ ▒ ░░    ░       ░░░ ░ ░  ░    ░    ░   ")
    print(Fore.RED + "         ░ ░                 ░      ░         ░  ░")
    print(Fore.RED + "         ░ ░                             ░        ")

def baixar_video(url, caminho_saida):
    try:
        yt = YouTube(url)
        stream_video = yt.streams.get_highest_resolution()
        caminho_destino = f"{caminho_saida}/{yt.title}.mp4"
        stream_video.download(caminho_saida)
        print(Fore.GREEN + "Download do vídeo feito com sucesso!")
        return caminho_destino
    except Exception as e:
        print(Fore.RED + "Erro ao baixar o vídeo:", str(e))
        return None

def converter_video_para_audio(url_video, caminho_saida):
    try:
        yt = YouTube(url_video)
        stream_video = yt.streams.get_highest_resolution()
        caminho_video = stream_video.download()
        titulo_video = yt.title
        caminho_audio = f"{caminho_saida}/{titulo_video}.mp3"
        clip_video = AudioSegment.from_file(caminho_video)
        clip_video.export(caminho_audio, format="mp3")
        print(Fore.GREEN + "Conversão do vídeo para áudio feita com sucesso!")
        return caminho_audio
    except Exception as e:
        print(Fore.RED + "Erro ao converter o vídeo para áudio:", str(e))
        return None

def baixar_video_threaded(url, caminho_saida):
    thread = threading.Thread(target=baixar_video, args=(url, caminho_saida))
    thread.start()

def converter_video_para_audio_threaded(url_video, caminho_saida):
    thread = threading.Thread(target=converter_video_para_audio, args=(url_video, caminho_saida))
    thread.start()

if __name__ == "__main__":
    imprimir_banner()
    print(Fore.RED + "├── 1 Baixar vídeo.")
    print(Fore.RED + "├── 2 Baixar música.")
    opcao = input(Fore.RED + "└──> Escolha a opção: ")

    if opcao == "1":
        url_video = input(Fore.RED + "Informe a URL do vídeo: ")
        caminho_saida = "/storage/emulated/0/Download/meu_pytube_video"
        baixar_video_threaded(url_video, caminho_saida)
    elif opcao == "2":
        url_video = input(Fore.RED + "Informe a URL do vídeo que deseja converter: ")
        caminho_saida = "/storage/emulated/0/Download/meu_pytube_musica"
        converter_video_para_audio_threaded(url_video, caminho_saida)
