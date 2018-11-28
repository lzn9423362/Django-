from bs4 import BeautifulSoup
import requests

start_url = 'https://bj.58.com/sale.shtml'

def get_channel_url(url):
    wb_data = requests.get(start_url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('.ym-submnu > li > b > a')
    for link in links:
        page_url = 'http://bj.58.com' + link.get('href')
        print(page_url)

get_channel_url(start_url)