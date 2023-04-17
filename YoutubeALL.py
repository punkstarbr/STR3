import youtube_dl

# Defina a URL do vídeo
video_url = 'https://vimeo.com/818191556'

# Defina o nome do arquivo de saída
output_file = 'AMOR.m3u'

# Defina as opções para o youtube_dl
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
    'outtmpl': output_file,
    'forcefilename': True
}

# Crie o objeto youtube_dl
ydl = youtube_dl.YoutubeDL(ydl_opts)

# Baixe as informações do vídeo e salve em um arquivo M3U
info_dict = ydl.extract_info(video_url, download=False)
with open(output_file, 'w') as f:
    f.write('#EXTINF:-1,' + info_dict['title'] + '\n')
    f.write(info_dict['formats'][0]['url'] + '\n')
