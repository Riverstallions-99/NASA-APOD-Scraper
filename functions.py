import shutil
import urllib.request
import ssl
import os

ssl._create_default_https_context = ssl._create_unverified_context

from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

options = FirefoxOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')


def fetchImage(url):
    driver = webdriver.Firefox(options=options)
    driver.get(url)
    try:
        image = driver.find_element(By.TAG_NAME, 'img')
        imageSrc = image.get_attribute("src")
        imageName = imageSrc[38:]
    except NoSuchElementException:
        print("An image was not found on this page... moving on!")
        driver.quit()
        exit()
    fileList = os.listdir('apodImages')
    if (imageName) in fileList:
        print("Image already exists, ignoring...")
    else:
        urllib.request.urlretrieve(imageSrc, imageName)
        original = r'C:/Users/white/PycharmProjects/Web Scraping Project/' + imageName
        target = r'C:/Users/white/PycharmProjects/Web Scraping Project/apodImages'
        shutil.move(original, target)
    driver.quit()
