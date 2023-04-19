import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def display_screenshot(driver, folder_name, filename):
    create_folder(folder_name)
    file_path = os.path.join(folder_name, filename)
    driver.save_screenshot(file_path)
    print(f"Screenshot saved as {file_path}")

def extract_m3u8_link(driver):
    time.sleep(30)
    log_entries = driver.execute_script("return window.performance.getEntries();")

    links = []
    for entry in log_entries:
        if ".m3u8" in entry['name']:
            print(entry['name'])
            links.append(entry['name'])

    return links

m3u8_links = extract_m3u8_link(driver)
print(f"m3u8 links: {m3u8_links}")

def generate_playlist(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    time.sleep(15)
    display_screenshot(driver, "MASTER", "screenshot1.png")

    #button = driver.find_element(By.XPATH, '//a[contains(@class, "wp-block-button__link") and contains(text(), "ACOMPANHE A CASA")]')
    #ActionChains(driver).click(button).perform()

    time.sleep(15)
    display_screenshot(driver, "MASTER", "screenshot2.png")

    m3u8_link = extract_m3u8_link(driver)
    print(f"m3u8 link: {m3u8_link}")

    driver.quit()

url = "https://ghenvivo.com/bbb"
generate_playlist(url)
