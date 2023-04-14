import subprocess

url = "https://www.bilibili.com/video/BV1qE411o7Zs/?spm_id_from=333.788.recommend_more_video.11"
command = ["youtube-dl", "-s", "--dump-json", url]
result = subprocess.check_output(command, universal_newlines=True)

# extrair o título e a duração do vídeo
for line in result.split("\n"):
    if line.strip():
        data = eval(line.strip())
        title = data["title"]
        duration = data["duration"]
        break

# salvar informações em formato EXTINF
with open("./BILIBILI.m3u", "w") as f:
    f.write(f"#EXTINF:{duration},{title}\n{url}")
