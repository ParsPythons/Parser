from bs4 import BeautifulSoup as BS
from time import sleep
import requests

print("Эта программа находится в тестировании, если найдётся ошибка отправьте на: parsprogram@yandex.ru")


def sleep_func(secn):
    if secn == "":
        print("Ошибка 001!")
        print("Измините время ожидания!!!")

    with open("sleep_time.txt", "w") as file:
        file.write(secn)
    print("Закончено!")


def sleep_time():
    with open("sleep_time.txt", "r") as file:
        times = file.read()
    try:
        times = int(times)
        return times
    except:
        print("Ошибка 002!")
        print("Измините время ожидания!!!")


def parse_main_page(linkis="https://www.yandex.ru", x=1):
    # Запрос на страницу
    response = requests.get(linkis).text
    # Задействуем библиотеку bs4
    soup = BS(response, "html.parser")
    # Выбираем нужные блоки
    reg = soup.find("span", class_="news__tab-text")
    news = soup.find_all("span", class_="news__item-inner")

    # Выводим "СМИ"
    print(f"{reg.text} :")

    # Цикл, для отдельного вывода новостей
    for themes in news:
        themes = themes.find("span", class_="news__item-content")

        if themes is not None:
            print(str(x) + ". " + str(themes.text))
            print("===")
            timed = sleep_time()
            sleep(timed)
            x += 1

"""
region = soup.find_all("span", class_="news__tab-text")
for news in region:
    print(news.text)
"""


def print_smi_news():
    request = requests.get("https://yandex.ru").text
    soup = BS(request, "html.parser")
    url = soup.find("a", class_="home-link2 home-link2_color_blue home-link2_hover_red news__tab news__tab_selected_yes mix-tabber__tab mix-tabber__tab_selected_yes")
    sublink = url.get("href")
    recponce = requests.get(sublink).text
    sup = BS(recponce, "html.parser")
    SMI = sup.find_all("a", class_="mg-card__link")
    for newsmi in SMI:
        newsmi = newsmi.find("h2", class_="mg-card__title")
        print(newsmi.text)
        print("===")
        timew = sleep_time()
        sleep(timew)


print("Это парсер. Его функция заключается в нахождении новостей.")
bol = True

while bol:
    print("Вывести новости с главной страницы 'Яндекс' (1)")
    print("Вывести новости СМИ (2)")
    print("Задать время ожидания (3)")
    print("Выход (4)")
    vr = input(">> ").strip()
    if vr == "1":
        parse_main_page()

    elif vr == "2":
        print_smi_news()

    elif vr == "3":
        print("Сколько секунд надо ждать?")
        print("Нажмите Enter, если хотите вернуться!")
        sec = input("").strip()
        if sec != "":
            sleep_func(sec)
        else:
            print("Пропущено!")
            
    else:
        bol = False
