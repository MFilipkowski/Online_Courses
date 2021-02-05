from bs4 import BeautifulSoup, NavigableString, Tag
from requests import get
import re
import csv


def nazwa_Kursu():
    URL = 'https://videopoint.pl/kategorie/programowanie'
    page = get(URL)
    amusements_soup = BeautifulSoup(page.content, "html.parser")
    bs = amusements_soup.findAll('div', {'class': 'book-list-inner'})[1]
    nazwa_lista = []
    # pobieranie nazwy kursu
    for item in bs:
        if isinstance(item, NavigableString):
            continue
        if isinstance(item, Tag):
            names = item.findAll('h2')

        for i in names:
            nazwa_lista.append(i.text)
    return nazwa_lista


# pobieranie cen kursow
def cena_kursu():
    URL = 'https://videopoint.pl/kategorie/programowanie'
    page = get(URL)
    amusements_soup = BeautifulSoup(page.content, "html.parser")
    bs = amusements_soup.findAll('div', {'class': 'book-list-inner'})[1]
    lista_cen = []

    # pobieranie nazwy kursu
    for price in bs.findAll('p', {'class': 'price price-add'}):
        for a in price.findAll('a', href=True):
            lista_cen.append(a.text.rstrip().lstrip())
    # print(len(lista_cen))
    # print(lista_cen)
    return lista_cen

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


def szczegoly():
    url_list = generator_linkow()
    row = []
    counter = 0
    for i in url_list:
        URL_2 = i
        Page = get(URL_2)
        soup = BeautifulSoup(Page.content, "html.parser")
        details = soup.find('div', {'class': 'details-box menu-section-item'})

        duration = details.find("dt", text='Czas trwania:').find_next('dd').text
        format = details.find("dt", text='Format:').find_next('dd').text
        data_wydania = details.find("dt", text='Data wydania :').find_next('dd').text
        ISBN = details.find("dt", text='ISBN :').find_next('dd').text
        numer_katalogowy = details.find("dt", text='Numer z katalogu:').find_next('dd').text
        rok_nagrania = details.find("dt", text='Rok nagrania:').find_next('dd').text.lstrip().rstrip()
        kategorie = details.select('li > span > a')[0].text
        autor = soup.find('dl', {'class': 'author'}).find_next('dd').text
        bigger_img = soup.find('div', {'class': 'cover-col video-col'})
        images = bigger_img.find('img')
        images = images['src']
        isActive = "100"
        ilosc = "1"
        visibility = "both"
        # print(duration, format, data_wydania, ISBN, numer_katalogowy, rok_nagrania, kategorie, autor, images)
        # row.append([duration, format, data_wydania, ISBN, numer_katalogowy, rok_nagrania, kategorie, autor, images])

        #OPIS KURSU
        opis = soup.find('div', {'class': 'text'}, itemprop='description').text
        opis = opis.replace("\n", ". ")
        opis = opis[1::].replace("\n", ". ")
        opis = opis[1::].replace("#", "Sharp ")
        opis_short = ".".join(opis.split(".")[:6])
        if len(opis_short) > 800:
            opis_short = ".".join(opis.split(".")[:5])
            opis_long = ".".join(opis.split(".")[6:])[1::]
        else:
            opis_long = ".".join(opis.split(".")[7:])[1::]
        #POBIERANIE WARTOŚCI Z INNYCH METOD

        nazwa_kursu_lista = nazwa_Kursu()
        cena_kursu_lista = cena_kursu()
        tmp_nazwa = nazwa_kursu_lista[counter]
        tmp_nazwa = tmp_nazwa.replace("#", "Sharp ")
        if len(tmp_nazwa) > 128:
            tmp_nazwa = ".".join(tmp_nazwa.split(".")[:3])
        tmp_cena = cena_kursu_lista[counter]
        row.append(
            [tmp_nazwa, tmp_cena, isActive, visibility, ilosc, data_wydania, kategorie, images, opis_short, opis_long])
        # tmp = (
        # [tmp_nazwa,tmp_cena, duration, format, data_wydania, ISBN, numer_katalogowy, rok_nagrania, kategorie, autor, images,opis])
        print(row)
        # with open('file.csv', 'a', newline='', encoding='utf-16') as f:
        #     fieldnames = ['nazwa kursu', 'cena kursu', 'czas', 'format', 'data', 'ISBN','katalogowy numer', 'rok nagrania', 'kategorie', 'autor', 'link']
        #     writer = csv.DictWriter(f, fieldnames=fieldnames)
        #     writer.writeheader()
        #     writer.writerow({'nazwa kursu' : tmp_nazwa, 'cena kursu' : tmp_cena, 'czas' : duration, 'format' : format, 'data' : data_wydania, 'ISBN' : ISBN,'katalogowy numer' : numer_katalogowy, 'rok nagrania' : rok_nagrania, 'kategorie' : kategorie, 'autor' : autor, 'link' : images})
        #     counter += 1

        with open('file.csv', 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow(row[counter])
            counter += 1

szczegoly()
