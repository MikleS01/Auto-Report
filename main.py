import requests
import re 
from pprint import *
from bs4 import BeautifulSoup
from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
import random
import os
import shutil

def times14():
    style = doc.styles['Normal']
    style.font.name = 'Times New Roman'
    style.font.size = Pt(14)

def clear_folder(folder_path):
    shutil.rmtree(folder_path)
    os.mkdir(folder_path)   






url = "https://ru.wikipedia.org/wiki/%D0%95%D0%BB%D1%8C%D1%86%D0%B8%D0%BD,_%D0%91%D0%BE%D1%80%D0%B8%D1%81_%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2%D0%B8%D1%87"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers = headers)
response.raise_for_status()
soup = BeautifulSoup(response.text, features="html.parser")
 
Headline = soup.find("h1")
all_tags = soup.find_all(['p', 'h2',"h3",'h4','h5','img'])

# if "<p>" in str(all_tags[0]): 
#     pprint("test")
 
doc = Document()
times14()
head = doc.add_heading(Headline.text)
head.alignment = WD_ALIGN_PARAGRAPH.CENTER

    

    
for number,delete in enumerate(reversed(all_tags)):
    if "<p" in str(delete):
        print(number)
        break
not_empty_tags = all_tags[0:-number]


os.makedirs("WikiPhoto", exist_ok = True)
clear_folder(folder_path = "WikiPhoto")   
for number,tag in  enumerate(not_empty_tags):    
    clear_text = re.sub(r'\[\d*\]', ' ', tag. text)
    if "<p" in str(tag): 
        clear_paragaphs = doc.add_paragraph(clear_text)
        clear_paragaphs.alignment = WD_ALIGN_PARAGRAPH.JUSTIFY
    elif "<h1" in str(tag):
        head1 = doc.add_heading(clear_text, level = 1)
        head1.alignment = WD_ALIGN_PARAGRAPH.CENTER 
    elif "<h2" in str(tag):
        head2 = doc.add_heading(clear_text, level = 2)
        head2.alignment = WD_ALIGN_PARAGRAPH.CENTER 
    elif '<h3' in str(tag):
        head3 = doc.add_heading(clear_text, level = 3)
        head3.alignment = WD_ALIGN_PARAGRAPH.CENTER 
    elif '<h4' in str(tag):
        head4 = doc.add_heading(clear_text, level = 4)
        head4.alignment = WD_ALIGN_PARAGRAPH.CENTER      
    elif '<h5' in str(tag):
        head5 = doc.add_heading(clear_text, level = 5)
        head5.alignment = WD_ALIGN_PARAGRAPH.CENTER 
    elif "<img" in str(tag):
        img_src = 'https:' + tag["src"]
        response = requests.get(img_src,headers = headers)
        response.raise_for_status()      
        with open(f'WikiPhoto/Photo{number}.png','wb') as file:
           file.write(response.content)
        img2 = doc.add_picture(f'WikiPhoto/Photo{number}.png')
        img2 = doc.paragraphs[-1] 
        img2.alignment = WD_ALIGN_PARAGRAPH.CENTER
     
doc.save('test.docx')


 