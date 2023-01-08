import os
from pytube import YouTube
from pytube import Playlist
from datetime import datetime
from tqdm import tqdm



def videos_separados(url_video,download_path = 'C:/Users/lautaro.delafuente/Downloads'):
   
    # Crea una instancia de YouTube con la URL del video
    yt = YouTube(url_video)

    print(yt)

    print(f'Descargando {yt.title}')

    # Obtiene los streams disponibles y filtra sólo los de mayor resolución de video
    video = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()

    # Descarga el video
    video.download(download_path)

    print('Descarga terminada')




def descargar_videos_playlist(url, output_path = 'C:/Users/lautaro.delafuente/Downloads'):
    playlist = Playlist(url)
    videos = playlist.video_urls

    print(f'Downloading: {playlist.title}')   

    for video in tqdm(videos):
        now = datetime.now()
        tiempo = now.strftime('%Y-%m-%d %H.%M.%S_')

        try:
            yt = YouTube(video)
        except:
            print(f'ERROR!! El Video {yt.title} no pudo descargarse, probamos con el siguiente.')
        else:
            stream = yt.streams.filter(progressive=True,file_extension='mp4').order_by('resolution').desc().first().download(output_path=output_path)
            #stream.download(output_path=output_path)
            print(f'El video {yt.title} fue descargado a las {tiempo}!')
    
    print('Descarga terminada')


#descargar_videos_playlist('','')

#videos_separados('')

