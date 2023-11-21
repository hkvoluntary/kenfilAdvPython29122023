from selenium import webdriver # pip install selenium
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import time


# Latitude of Dave's office.
office_lat = 41.980262

def distance(lat1, lat2):
    'Return approx miles between lat1 and lat2'
    return 69 * abs(lat1 - lat2)

driver = webdriver.Firefox()
# Set of bus ids that you want to monitor.

busids = '8123' # Get it from https://www.ctabustracker.com/map
api_key = ''
url_string = "https://www.ctabustracker.com/bustime/api/v2/getvehicles?key=" + api_key + "&vid=" + busids



latitude = ""
longitude = ""
vehicle_id = ""
route = ""
dist = 0
while True:
    with urlopen(url_string) as f:
        tree = ET.parse(f)
        root = tree.iter()
        for child in root:
            #print(child.tag, child.text, child.attrib)
            if child.tag == "lat" :
                latitude = child.text
                latitude_float = float(latitude)
            if child.tag == "lon" :
                longitude = child.text
                longitude_float = float(longitude)
            if child.tag == "vid":
                vehicle_id = child.text
            if child.tag == "rt":
                route = child.text

        dist = distance(latitude_float, office_lat)
        print('%s Latitude: %0.6f Longitude: %06.f Distance %0.6f miles' % (vehicle_id, latitude_float, longitude_float, dist))
        # Launch a browser to see on a map
        x = 'www.openstreetmap.org/?mlat=%f&mlon=%f&zoom=17' % (latitude_float, longitude_float)
        refreshrate = 5
        driver.get("http://" + x)
        time.sleep(refreshrate)
        # driver.refresh()
