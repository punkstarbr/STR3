from selenium import webdriver

url = "https://www.bilibili.com/video/BV1qE411o7Zs/?spm_id_from=333.788.recommend_more_video.11"
driver = webdriver.Chrome()  # precisa do ChromeDriver instalado

driver.get(url)

# extrair o título do vídeo
title = driver.find_element_by_class_name("video-title").text.strip()

# extrair a duração do vídeo
duration_tag = driver.find_element_by_css_selector("meta[itemprop='duration']")
duration = int(duration_tag.get_attribute("content")) // 1000

driver.quit()

# salvar informações em formato EXTINF
with open("BILIBILI.m3u", "w") as f:
    f.write(f"#EXTINF:{duration},{title}\n{url}")
