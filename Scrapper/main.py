from bs4 import BeautifulSoup, NavigableString, Tag
from requests import get
import re
import csv


def generator_linkow():
    URL = 'https://videopoint.pl/kategorie/programowanie'
    page = get(URL)
    amusements_soup = BeautifulSoup(page.content, "html.parser")
    bs = amusements_soup.findAll('div', {'class': 'book-list-inner'})[1]
    list = []
    for item in bs.findAll('a', href=True):
        if item.text:
            if 'zakupy' in item['href']:
                continue
            else:
                c = "http:" + item['href']
                if c in list:
                    continue
                else:
                    list.append("http:" + item['href'])
                    # print("http:" + item['href'])
                    # print(list)
    return list


def kategorie():
    url_list = generator_linkow()
    row = []
    counter = 0
    for i in url_list:
        URL_2 = i
        Page = get(URL_2)
        soup = BeautifulSoup(Page.content, "html.parser")
        details = soup.find('div', {'class': 'details-box menu-section-item'})
        kategorie = details.select('li > span > a')[0].text
        kategorie = kategorie+';'
        if [kategorie] in row:
            continue
        else:
            row.append([kategorie])
        print(row)
        with open('kategorie.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=",")
            writer.writerow(row[counter])
            counter += 1


kategorie()
