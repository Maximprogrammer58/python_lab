from bs4 import BeautifulSoup
import requests
import os

parser_data_list = []

URL = "https://www.gismeteo.ru/diary/4618/2023/8/"
html_page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(html_page.text, 'lxml')

month_and_year = soup.title.text.split()
month, year = month_and_year[7], month_and_year[8]

for element in soup.find_all('td', class_="first"):
    temp = element.find_next()
    press = temp.find_next()
    wind = press.find_next_sibling().find_next_sibling().find_next_sibling()
    parser_data_list.append([[int(year), month, int(element.text)], [
        temp.text, press.text, wind.text]])

print(parser_data_list)