from pytube import YouTube
from pydub import AudioSegment
from colorama import Fore

def banner():
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

banner()

def on_progresso(stream, chunk, bytes_restantes):
    total_bytes = stream.filesize
    bytes_baixados = total_bytes - bytes_restantes
    progresso = (bytes_baixados / total_bytes) * 100
    print(Fore.BLUE + f"Progresso: {progresso:.2f}%")

def baixar_video(url, caminho_saida):
    try:
        yt = YouTube(url)
        stream_video = yt.streams.get_highest_resolution()
        caminho_destino = caminho_saida + "/" + yt.title + ".mp4"
        stream_video.download(caminho_saida)
        return caminho_destino
    except Exception as e:
        print("Erro ao baixar o vídeo:", str(e))
        return None

def youtube_para_audio(url_video, caminho_saida):
    try:
        yt = YouTube(url_video, on_progress_callback=on_progresso)
        stream_video = yt.streams.get_highest_resolution()
        caminho_video = stream_video.download()
        titulo_video = yt.title
        clip_video = AudioSegment.from_file(caminho_video)
        caminho_audio = caminho_saida + titulo_video + ".mp3"
        clip_video.export(caminho_audio, format="mp3")
        return caminho_audio
    except Exception as e:
        print(Fore.RED + "Erro ao converter o vídeo para áudio:", str(e))
        return None

if __name__ == "__main__":
    print(Fore.RED + "1 - Baixar vídeo.")
    print(Fore.RED + "2 - Baixar música.")
    opcao = input(Fore.RED + "Escolha a opção: ")

    if opcao == "1":
        url_video = input(Fore.RED + "Informe a URL do vídeo: ")
        caminho_saida = "/storage/emulated/0/Download"
        arquivo_baixado = baixar_video(url_video, caminho_saida)

        if arquivo_baixado:
            print(Fore.GREEN + "Vídeo baixado com sucesso:", arquivo_baixado)
        else:
            print(Fore.RED + "Falha ao baixar o vídeo.")
    elif opcao == "2":
        url_video = input(Fore.RED + "Informe a URL do vídeo que deseja converter: ")
        caminho_saida = "/storage/emulated/0/Download/teste"
        arquivo_audio = youtube_para_audio(url_video, caminho_saida)

        if arquivo_audio:
            print(Fore.GREEN + "Vídeo convertido para áudio com sucesso. Arquivo de áudio salvo em:", arquivo_audio)
        else:
            print(Fore.RED + "Falha ao converter o vídeo para áudio.")
