from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
import time


def start_driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver


def capture_screenshot(url, file_name):
    driver = start_driver()
    driver.get(url)
    time.sleep(3)  
    driver.save_screenshot(file_name)
    driver.quit()


def capture_screenshots_from_file(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
        for idx, url in enumerate(urls):
            url = url.strip()
            if url:
                capture_screenshot(url, f'screenshot_{idx + 1}.png')


choice = input("1: Tek URL, 2: URL Dosyası -> Seçiminizi yapın: ")

if choice == '1':
    url = input("Lütfen URL'yi girin: ")
    capture_screenshot(url, 'screenshot.png')
    print("Ekran görüntüsü alındı: screenshot.png")
elif choice == '2':
    file_path = input("Lütfen TXT dosyasının yolunu girin: ")
    capture_screenshots_from_file(file_path)
    print("Tüm URL'ler için ekran görüntüleri alındı.")
else:
    print("Geçersiz seçim yaptınız!")
