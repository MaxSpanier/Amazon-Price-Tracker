import requests
from bs4 import BeautifulSoup
from datetime import datetime 
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Brave Chrome/77.0.3865.90 Safari/537.36'}

#gets the html code from the given url and returns it in soup
def get_html_data(url):
    html_data = requests.get(url, headers=headers)
    soup = BeautifulSoup(html_data.content, 'html.parser')
    return soup

#takes soup and searches for the given id
def get_name(soup):
    name = soup.find(id='productTitle').get_text()
    return name.strip()

#takes soup and searches for the given id
def get_price(soup):
    price = soup.find(id='priceblock_ourprice').get_text()
    return price.strip()

#returns the current time in dd-mm-yyyy hh:mm:ss
def get_time():
    cd = datetime.now()
    return cd.strftime('%d-%m-%Y %H:%M:%S')

#scrapes the website by calling alls the methods above and returns the name and price of the product as well as the current time
def scrape(url):
    soup = get_html_data(url)
    name = get_name(soup)
    price = get_price(soup)
    date = get_time()
    return name, price, date
