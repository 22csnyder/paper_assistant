"""extract_shared_links.py"""


import os, re, requests, time


# from bs4 import BeautifulSoup


import requests
from lxml import html

# URL of the OneTab page
url = "https://www.one-tab.com/page/ey5fAcuZSsyR1sGs1k267g"

# Send a GET request to fetch the page content
response = requests.get(url)
if response.status_code == 200:
    # Parse the HTML content
    tree = html.fromstring(response.content)
    
    # Extract all href attributes from anchor tags
    urls = tree.xpath('//a/@href')
    
    # Print the extracted URLs
    for url in urls:
        print(url)
else:
    print("Failed to fetch the page:", response.status_code)
