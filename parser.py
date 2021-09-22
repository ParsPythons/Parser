from bs4 import BeautifulSoup as BS
from time import sleep
import os
import requests

print("Эта программа находится в тестировании, если найдётся ошибка отправьте на: parsprogram@yandex.ru")


def check_wifi():
    # Проверка подключения к сети
    try:
        requests.get("https://www.yandex.ru/")
        return True
    except:
        print("Сеть вай фай не обнаружена!!!")
        return False


def check_version():
    # Проверка обновлений
    ver_txt = "https://github.com/ParsPythons/Parser/blob/main/version.txt"
    github = "https://github.com/ParsPythons/Parser.git"
    ver = requests.get(ver_txt).text
    sop = BS(ver, "html.parser")
    version = sop.find("td", class_="blob-code blob-code-inner js-file-line").text
    with open("version.txt", "r") as vers:
        only_ver = vers.read()
    print(f"Текущая версия: {only_ver}")
    print(f"Версия на сайте: {version}")
    if version != only_ver:
        print("Есть обновление, не хотите обновиться? (y/n)")
        upgrade = input("> ").strip().lower()
        if upgrade == "y":
            # Обновление
            path = os.getcwd()
            os.chdir(path[:-6])
            print("Идёт обновление, подождите...")
            os.system("rm -R Parser")
            os.system("git clone " + github)
            os.chdir(path)
            with open("version.txt", "w") as new_ver:
                new_ver.write(version)


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


def parse_main_page(x=1):
    # Запрос на страницу
    response = requests.get("https://www.yandex.ru").text
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


def print_smi_news(x=1):
    request = requests.get("https://yandex.ru").text
    soup = BS(request, "html.parser")
    url = soup.find("a", class_="home-link2 home-link2_color_blue home-link2_hover_red news__tab news__tab_selected_yes mix-tabber__tab mix-tabber__tab_selected_yes")
    sublink = url.get("href")
    recponce = requests.get(sublink).text
    sup = BS(recponce, "html.parser")
    SMI = sup.find_all("a", class_="mg-card__link")
    for newsmi in SMI:
        newsmi = newsmi.find("h2", class_="mg-card__title")
        print(str(x) + ". " + newsmi.text)
        print("===")
        timew = sleep_time()
        sleep(timew)
        x += 1


print("Это парсер. Его функция заключается в нахождении новостей.")
bol = True

# Цикл
while bol:
    Wifi = check_wifi()
    if Wifi == True:
        check_version()
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

    else:
        bol = False
