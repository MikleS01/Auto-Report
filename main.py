import requests
from pprint import *
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt


url = 'https://ru.wikipedia.org/wiki/Rust_(%D0%B8%D0%B3%D1%80%D0%B0)'

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers = headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, features="html.parser")

Headline = soup.find("h1")
All_paragraphs = soup.find_all('p')

for i in All_paragraphs:
    pprint(i.text)


pprint(Headline.text)
