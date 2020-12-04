#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

vessels_in_port = pd.read_csv(
    '/Users/Traky/Desktop/Projects/random/web-scraping/Hamilton Vessels/vessels_in_port.csv'
)

# url of the main page
url = "https://www.hopaports.ca/locations/port-of-hamilton/vessel-tracking/"
req = requests.get(url)
soup = BeautifulSoup(req.content, "html.parser")

# get headers
header = []
tbl_head = soup.find(id="vessels-in-port").select('thead th b')
for head in tbl_head:
    header.append(head.get_text())  # removes <b></b>

# vessels in port, table data
tdata = soup.find(id="vessels-in-port").select('td')

# strip tag
data = []
for td in tdata:
    data.append(td.get_text())

# today's data in a dataframe
data_today = pd.DataFrame(np.array(data).reshape(int(len(data) / 10), 10),
                          columns=header)

# append
vessels_in_port = vessels_in_port.append(data_today, ignore_index=True)

# remove duplicates
vessels_in_port = vessels_in_port.drop_duplicates()

# export
vessels_in_port.to_csv('vessels_in_port.csv', index=False)
