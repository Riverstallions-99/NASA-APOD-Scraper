import shutil
import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions

#from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

# -------------------------------------------------------------------
options = FirefoxOptions()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
options.add_argument('--headless')
# -------------------------------------------------------------------
url = "http://apod.nasa.gov/apod"
# Run the driver, using firefox, with the options as above
driver = webdriver.Firefox(options=options)
driver.get(url)
# -------------------------------------------------------------------
image = driver.find_element(By.TAG_NAME, 'img')
imageSrc = image.get_attribute("src")
imageName = imageSrc[38:]
print(imageSrc)
print(imageName)
urllib.request.urlretrieve(imageSrc, imageName)
# -------------------------------------------------------------------
driver.quit()
# \/ Moves the file into the apodImages folder, for use by the OS as wallpaper \/
original = r'C:/Users/white/PycharmProjects/Web Scraping Project/' + imageName
target = r'C:/Users/white/PycharmProjects/Web Scraping Project/apodImages'
try:
    shutil.move(original, target)
except Exception:
    print("Image already exists, exiting...")
    exit()
# Need to write an extra piece of code which will check for missing images, so:
# - Currently it just goes to today's date
# - Retrieve today/yesterday's date, create a URL request with yesterday's date, in the correct format
# - Attempt to download, or check if the file already exists, and keep going backwards in time, up to a certain point (when? - limit to 30 days)
# - apod.nasa.gov/apod/ap<year><month><day>.html for example: apod.nasa.gov/apod/ap240417.html

exit()
