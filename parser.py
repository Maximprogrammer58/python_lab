from bs4 import BeautifulSoup
import csv
import os
import requests


def month_conversion(month):
    months_list = {"Январь": "01", "Февраль": "02", "Март": "03", "Апрель": "04", "Май": "05", "Июнь": "06",
                   "Июль": "07", "Август": "08", "Сентябрь": "09", "Октябрь": "10", "Ноябрь": "11", "Декабрь": "12"}
    return months_list.get(month)


def parser():
    URL = "https://www.gismeteo.ru/diary/4618/2019/9/"
    html_page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(html_page.text, 'lxml')

    parser_data = []

    month_and_year = soup.title.text.split()
    month, year = month_conversion(month_and_year[7]), month_and_year[8]

    for day in soup.find_all('td', class_="first"):
        temp = day.find_next()
        press = temp.find_next()
        wind = press.find_next_sibling().find_next_sibling().find_next_sibling()
        parser_data.append([day.text + "." + month + "." + year,
                           temp.text+"°C", press.text+"мм.рт.ст.", wind.text])

    return parser_data


def upload_csv(parser_data):
    with open('dataset.csv', 'w', encoding="utf-8", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(parser_data)


upload_csv(parser())
