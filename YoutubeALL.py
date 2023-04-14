import subprocess

url = "https://www.bilibili.com/video/BV1qE411o7Zs/?spm_id_from=333.788.recommend_more_video.11"
command = ["yt-dlp", "--get-title", url]
result = subprocess.check_output(command, universal_newlines=True)

# extrair o título do vídeo
title = result.strip()

# salvar informações em formato EXTINF
with open("BILIBILI.m3u", "w") as f:
    f.write(f"#EXTINF:-1,{title}\n{url}")
