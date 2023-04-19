import os
import time
import tempfile
from PIL import Image as PILImage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def display_screenshot(driver):
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmpfile:
        driver.save_screenshot(tmpfile.name)
        img = mpimg.imread(tmpfile.name)
        plt.imshow(img)
        plt.show()


def generate_playlist(url):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")

    driver = webdriver.Chrome(options=chrome_options)

    driver.get(url)

    time.sleep(15)
    display_screenshot(driver)

    button = driver.find_element(By.XPATH, '//a[contains(@class, "wp-block-button__link") and contains(text(), "ACOMPANHE A CASA")]')
    ActionChains(driver).click(button).perform()

    time.sleep(15)
    display_screenshot(driver)

    driver.quit()

url = "https://bbbgratis.com/"
generate_playlist(url)
