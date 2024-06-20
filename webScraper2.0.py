import shutil
import time
import urllib.request
import ssl
import datetime
import os
from os import listdir
from os.path import isfile, join
from datetime import timedelta, date

ssl._create_default_https_context = ssl._create_unverified_context

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By

# -------------------------------------------------------------------
options = FirefoxOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
# -------------------------------------------------------------------
url = "http://apod.nasa.gov/apod"

driver = webdriver.Firefox(options=options)
driver.get(url)
try:
    image = driver.find_element(By.TAG_NAME, 'img')
    imageSrc = image.get_attribute("src")
    imageName = imageSrc[38:]
except NoSuchElementException:
    print("An image was not found on this page... moving on!")
fileList = os.listdir('apodImages')
if (imageName) in fileList:
    print("Image already exists, ignoring...")
else:
    urllib.request.urlretrieve(imageSrc, imageName)
    # \/ Moves the file into the apodImages folder, for use by the OS as wallpaper \/
    original = r'C:/Users/white/PycharmProjects/Web Scraping Project/' + imageName
    target = r'C:/Users/white/PycharmProjects/Web Scraping Project/apodImages'
    shutil.move(original, target)
driver.quit()



# Second loop of code, to go backwards in time to check previous stuff, say if your PC has been off for a long time
dateCheck = datetime.date.today()
endDate = datetime.date(2024, 6, 5)

while dateCheck != endDate:
    dateCheck = dateCheck + timedelta(days=-1)
    formattedDate = dateCheck.strftime("%y%m%d")
    driver = webdriver.Firefox(options=options)
    driver.get(url + "/ap" + formattedDate + ".html")
    try:
        image = driver.find_element(By.TAG_NAME, 'img')
        imageSrc = image.get_attribute("src")
        imageName = imageSrc[38:]
    except NoSuchElementException:
        print("An image was not found on this page... moving on!")
    fileList = os.listdir('apodImages')
    if (imageName) in fileList:
        print("Image already exists, continuing to next date..." + dateCheck.strftime("%d/%m/%y"))
    else:
        urllib.request.urlretrieve(imageSrc, imageName)
        # \/ Moves the file into the apodImages folder, for use by the OS as wallpaper \/
        original = r'C:/Users/white/PycharmProjects/Web Scraping Project/' + imageName
        target = r'C:/Users/white/PycharmProjects/Web Scraping Project/apodImages'
        shutil.move(original, target)
    driver.quit()
print("Checked all images until the date of " + endDate.strftime("%d/%m/%y") + ".")
driver.quit()
exit()
