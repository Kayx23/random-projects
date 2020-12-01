# import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# webdriver
driver = webdriver.Chrome()
driver.get(
    'https://www.amazon.ca/ProPOW-Changing-Remote-Control-Dimmable/dp/B07H6GC96V/ref=sxts_sxwds-bia-wc-p13n1_0?cv_ct_cx=rgb&dchild=1&keywords=rgb&pd_rd_i=B07H6GC96V&pd_rd_r=9b35fe6f-6b00-417b-a6e8-855f47f76b5e&pd_rd_w=98ukb&pd_rd_wg=wnVc6&pf_rd_p=153c9989-e6e2-49d3-8832-84a87124c284&pf_rd_r=BPE46HDS76AH557JYZQD&psc=1&qid=1604861966&sr=1-1-80ba0e26-a1cd-4e7b-87a0-a2ffae3a273c'
)
html = driver.page_source

# make soup
soup = BeautifulSoup(html, 'html.parser')

# get info
title = soup.find(id='productTitle').get_text().strip()
price = soup.find(id="priceblock_dealprice").get_text()  # 'CDN$\xa020.79'
price = price.replace(u'\xa0', u' ')  # replace \xa0, the no break space

# float(price.split()[1])
