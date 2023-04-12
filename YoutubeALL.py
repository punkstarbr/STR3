import subprocess
import time
import os
import yt_dlp
import youtube_dl

# Read the links from the YOUTUBEALL.txt file
try:
    with open('YOUTUBEALL.txt', 'r') as f:
        links = [line.strip() for line in f.readlines()]
except Exception as e:
    print(f"Error reading the YOUTUBEALL.txt file: {e}")
    links = []

banner = r'''
#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"
#EXTM3U x-tvg-url="https://raw.githubusercontent.com/Nicolas0919/Guia-EPG/master/GuiaEPG.xml"
'''

# Install yt-dlp
subprocess.run(['pip', 'install', '--upgrade', 'yt-dlp'])

# Define options for yt-dlp
ydl_opts_yt_dlp = {
    'format': 'best',  # Get the best quality

    'write_all_thumbnails': False,  # Don't download thumbnails
    'skip_download': True,  # Don't download the video
}

# Define options for youtube-dl
ydl_opts_youtube_dl = {
    'format': 'best',  # Get the best quality

    'writethumbnail': False,  # Don't download thumbnails
    'skip_download': True,  # Don't download the video
}

# Get the playlist and write to file
try:
    with open('./LISTA5YTALL.m3u', 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        f.write(banner)
        for i, link in enumerate(links):
            try:
                with yt_dlp.YoutubeDL(ydl_opts_yt_dlp) as ydl:
                    info = ydl.extract_info(link, download=False)
            except yt_dlp.utils.DownloadError:
                with youtube_dl.YoutubeDL(ydl_opts_youtube_dl) as ydl:
                    info = ydl.extract_info(link, download=False)
            except Exception as e:
                print(f"Error processing the link {link}: {e}")
                continue

            if 'url' not in info:
                print(f"Error writing video information for {link}: 'url'")
                continue

            url = info['url']
            thumbnail_url = info['thumbnail']
            description = info.get('description', '')[:10]
            title = info.get('title', '')
            f.write(f"#EXTINF:-1 group-title=\"YOUTUBE\" tvg-logo=\"{thumbnail_url}\",{title} - {description}...\n")
            f.write(f"{url}\n")
            f.write("\n")
except Exception as e:
    print(f"Error creating the .m3u8 file: {e}")

