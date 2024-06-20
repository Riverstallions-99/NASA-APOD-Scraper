import ssl
import datetime
from datetime import timedelta
from functions import fetchImage

ssl._create_default_https_context = ssl._create_unverified_context

# --User Options-----------------------------------------------------
correctMissedImages = False
endDate = datetime.date(2024, 6, 7)

# Fetch today's NASA APOD
url = "http://apod.nasa.gov/apod"
fetchImage(url)

# Second loop of code, to go backwards in time to check previous stuff, say if your PC has been off for a long time
if correctMissedImages:
    dateCheck = datetime.date.today()
    while dateCheck != endDate:
        dateCheck = dateCheck + timedelta(days=-1)
        formattedDate = dateCheck.strftime("%y%m%d")
        fetchImage(url + "/ap" + formattedDate + ".html")
    print("Checked all images until the date of " + endDate.strftime("%d/%m/%y") + ".")
exit()
