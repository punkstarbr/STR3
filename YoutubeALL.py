import youtube_dl

# Crie uma lista com as URLs dos canais
channels = [
    'https://vimeo.com/user125724700',
    'https://vimeo.com/user191718673',
    'https://vimeo.com/poupainvest',
    'https://vimeo.com/user132917313'
]

# Defina a pasta de destino
dest_folder = '/content/drive/MyDrive/HOJE/QUINTA/'

# Defina as opções para o youtube_dl
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': dest_folder,
}

# Crie o objeto youtube_dl
ydl = youtube_dl.YoutubeDL(ydl_opts)

# Percorra cada URL do canal e baixe os vídeos
for channel in channels:
    ydl.download([channel])

# Baixe as informações do vídeo e salve em um arquivo M3U
info_dict = ydl.extract_info(video_url, download=False)
with open(output_file, 'w') as f:
    f.write('#EXTINF:-1,' + info_dict['title'] + '\n')
    f.write(info_dict['formats'][0]['url'] + '\n')
