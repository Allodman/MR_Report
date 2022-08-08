import lxml
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import pandas as pd
import json
import csv
import re
import glob
import os
import time

list_ip_cameras = ["https://videocam.online/Object/mrgroup.php?id=D1-1.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=D1-2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=IceFili.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=IceFili-OfficeSales.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=FiliCity2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=ilmensky.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=ilmensky3.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=ilmensky2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=ilmensky4.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Vidnoe4.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Vidnoe8.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Vidnoe01.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Vidnoe7.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Vidnoe02.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Metropolia1.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Metropolia2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Metropolia3.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Metropolia4.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Metropolia5.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Potapp.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Dubininsky1.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Dubininsky2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Setun.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=CityBay.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=CityBay2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=CityBay3.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=CityBay4.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Hutor.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=iCity.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=MOD1.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=MOD2.stream&width=1200&height=800&autoplay=true",
                   "https://videocam.online/Object/mrgroup.php?id=Slava.stream&width=1200&height=800&autoplay=true"
                 ]

ua = UserAgent()
uar = ua.random
headers = {
    "accept": '*/*',
    "user-agent": uar
}

# for url in list_ip_cameras:
url = list_ip_cameras[0]
rec = requests.get(url, headers=headers)
src = rec.text

with open()
