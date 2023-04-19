import subprocess
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

# Install yt-dlp and youtube-dl
subprocess.run(['pip', 'install', '--upgrade', 'yt-dlp'])
subprocess.run(['pip', 'install', '--upgrade', 'youtube_dl'])

# Define options for yt-dlp and youtube-dl
ydl_opts = {
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Get the best quality in mp4 format
    'format': 'best',  # Obtém a melhor qualidade


    'write_all_thumbnails': False,  # Don't download thumbnails
    'skip_download': True,  # Don't download the video
    'write_all_thumbnails': False,  # Não faz download das thumbnails
    'skip_download': True,  # Não faz download do vídeo
}


# Get the playlist and write to file
try:
    with open('./LISTA5YTALL.m3u', 'w', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        f.write(banner)
        for i, link in enumerate(links):
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=False)
            except Exception as e:
                print(f"yt-dlp failed for link {link}: {e}")
                print("Trying with youtube-dl...")
                try:
                    with youtube_dl.YoutubeDL(ydl_opts) as ydl_backup:
                        info = ydl_backup.extract_info(link, download=False)
                except Exception as e_backup:
                    print(f"youtube-dl failed for link {link}: {e_backup}")
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
    print(f"Error creating the .m3u file: {e}")

   
import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp


# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_youtube = "https://www.youtube.com/channel/UCYfdidRxbB8Qhf0Nx7ioOYw"

# Abrir a página desejada
driver.get(url_youtube)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page using ActionChains
while True:
    try:
        # Find the last video on the page
        last_video = driver.find_element_by_xpath("//a[@id='video-title'][last()]")
        # Scroll to the last video
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(1)
    except:
        break
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

time.sleep(5)

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-grid-video-renderer")
    links = ["https://www.youtube.com" + video.get("href") for video in videos]
    titles = [video.get("title") for video in videos]
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()





# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'yt dlp'])
subprocess.run(['pip', 'install', 'pytube'])


time.sleep(5)
from pytube import YouTube

# Define options for yt-dlp and youtube-dl
ydl_opts = {
    'format': 'best',  # Obtém a melhor qualidade
    'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]',  # Get the best quality in mp4 format




    'write_all_thumbnails': False,  # Don't download thumbnails
    'skip_download': True,  # Don't download the video
    'write_all_thumbnails': False,  # Não faz download das thumbnails
    'skip_download': True,  # Não faz download do vídeo
}
# Get the playlist and write to file
try:
    with open('./LISTA5YTALL.m3u', 'a', encoding='utf-8') as f:
        f.write("#EXTM3U\n")
        for i, link in enumerate(links):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(link, download=False)
            if 'url' not in info:
                print(f"Erro ao gravar informações do vídeo {link}: 'url'")
                continue
            url = info['url']
            thumbnail_url = info['thumbnail']
            description = info.get('description', '')[:10]
            title = info.get('title', '')
            f.write(f"#EXTINF:-1 group-title=\"NEWS WORLD\" tvg-logo=\"{thumbnail_url}\",{title} - {description}...\n")
            f.write(f"{url}\n")
            f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
    
    
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp

from pytube import YouTube

def generate_playlist(url_youtube):
    # Configuring Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Instanciando o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Abrir a página desejada
    driver.get(url_youtube)

    # Aguardar alguns segundos para carregar todo o conteúdo da página
    time.sleep(5)

    # Get the page source again after scrolling to the bottom
    html_content = driver.page_source

    time.sleep(5)

    # Find the links and titles of the videos found
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-video-renderer")
        links = ["https://www.youtube.com" + video.get("href") for video in videos]
        titles = [video.get("title") for video in videos]
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        # Close the driver
        driver.quit()

    # Define as opções para o youtube-dl
    ydl_opts = {
        'format': 'best',  # Obtém a melhor qualidade
        'write_all_thumbnails': False,  # Não faz download das thumbnails
        'skip_download': True,  # Não faz download do vídeo
    }

    # Get the playlist and write to file
    try:
        with open('./LISTA5YTALL.m3u', 'a', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            for i, link in enumerate(links):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=False)
                if 'url' not in info:
                    print(f"Erro ao gravar informações do vídeo {link}: 'url'")
                    continue
                url = info['url']
                thumbnail_url = info['thumbnail']
                description = info.get('description', '')[:10]
                title = info.get('title', '')
                f.write(f"#EXTINF:-1 group-title=\"NOTICIAS GRAVADAS\" tvg-logo=\"{thumbnail_url}\",{title} - {description}...\n")
                f.write(f"{url}\n")
                f.write("\n")
    except Exception as e:
        print(f"Erro ao criar o arquivo .m3u8: {e}")

url_youtube1 = "https://www.youtube.com/results?search_query=noticiero&sp=CAISBBABGAI%253D"
url_youtube2 = "https://www.youtube.com/results?search_query=telegiornale&sp=CAI%253D"
url_youtube3 = "https://www.youtube.com/results?search_query=telejornal&sp=CAISBBABGAI%253D"

generate_playlist(url_youtube1)
generate_playlist(url_youtube2)
generate_playlist(url_youtube3)

import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp

from pytube import YouTube

def generate_playlist(url_youtube):
    # Configuring Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    # Instanciando o driver do Chrome
    driver = webdriver.Chrome(options=chrome_options)

    # Abrir a página desejada
    driver.get(url_youtube)

    # Aguardar alguns segundos para carregar todo o conteúdo da página
    time.sleep(5)

    # Get the page source again after scrolling to the bottom
    html_content = driver.page_source

    time.sleep(5)

    # Find the links and titles of the videos found
    try:
        soup = BeautifulSoup(html_content, "html.parser")
        videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-video-renderer")
        links = ["https://www.youtube.com" + video.get("href") for video in videos]
        titles = [video.get("title") for video in videos]
    except Exception as e:
        print(f"Erro: {e}")
    finally:
        # Close the driver
        driver.quit()

    # Define as opções para o youtube-dl
    ydl_opts = {
        'format': 'best',  # Obtém a melhor qualidade
        'write_all_thumbnails': False,  # Não faz download das thumbnails
        'skip_download': True,  # Não faz download do vídeo
    }

    # Get the playlist and write to file
    try:
        with open('./LISTA5YTALL.m3u', 'a', encoding='utf-8') as f:
            f.write("#EXTM3U\n")
            for i, link in enumerate(links):
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(link, download=False)
                if 'url' not in info:
                    print(f"Erro ao gravar informações do vídeo {link}: 'url'")
                    continue
                url = info['url']
                thumbnail_url = info['thumbnail']
                description = info.get('description', '')[:10]
                title = info.get('title', '')
                f.write(f"#EXTINF:-1 group-title=\"USA NEWS\" tvg-logo=\"{thumbnail_url}\",{title} - {description}...\n")
                f.write(f"{url}\n")
                f.write("\n")
    except Exception as e:
        print(f"Erro ao criar o arquivo .m3u8: {e}")


url_youtube1 = "https://www.youtube.com/results?search_query=telemundo+noticiero&sp=CAISBhABGAIgAQ%253D%253D"
url_youtube2 = "https://www.youtube.com/results?search_query=univision+vivo&sp=CAISAhAB"
url_youtube3 = "https://www.youtube.com/results?search_query=voz+de+am%C3%A9rica+noticias&sp=CAISBBABGAI%253D"

generate_playlist(url_youtube1)
generate_playlist(url_youtube2)
generate_playlist(url_youtube3)
