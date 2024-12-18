import requests
from bs4 import BeautifulSoup

url = 'https://books.toscrape.com/'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}

page = requests.get(url, headers = headers)

type(page.text)

soup = BeautifulSoup(page.text, 'html.parser')

type (soup)