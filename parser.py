try:

    from bs4 import BeautifulSoup as BS
    from time import sleep
    import os
    import requests

    print("Эта программа находится в тестировании!")

    request = requests.get("https://yandex.ru").text


    # Начинаются функции
    def choise_source_site():
        print("Яндекс (Y) или Google (G) ?: ")
        choise = input("> ").strip().lower()
        if choise == "y":
            return "yandex"
        else:
            return "google"


    def check_wifi():
        # Проверка подключения к сети
        try:
            requests.get("https://www.yandex.ru/")
            return True
        except:
            print("Сеть вай фай не обнаружена!!!")
            return False


    def upgrade_program():
        print("Удалите файл .git!")
        print("Нажмите Enter когда удалите...")
        input("")
        github = "https://github.com/ParsPythons/Parser.git"
        path = os.getcwd()
        os.chdir(path[:-6])
        os.system("rm -R Parser")
        os.system("git clone " + github)
        os.chdir(path)


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
        if version != only_ver.strip():
            print("Есть обновление, не хотите обновиться? (y/n)")
            chse = input("> ").strip().lower()
            if chse == "y":
                print("Удалите файл .git!")
                print("Нажмите Enter когда удалите...")
                input("")
                # Обновление
                path = os.getcwd()
                os.chdir(path[:-6])
                print("Идёт обновление, подождите...")
                os.system("rm -R Parser")
                os.system("git clone " + github)
                os.chdir(path)
                with open("version.txt", "w") as new_ver:
                    new_ver.write(version)


    def clear_news():
        os.system("clear")


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
            times = int(times.strip())
            return times
        except:
            print("Ошибка 002!")
            print("Измините время ожидания!!!")


    timed = sleep_time()


    def google_russia_news(x=1):
        response = requests.get(
            "https://news.google.com/topics/CAAqIQgKIhtDQkFTRGdvSUwyMHZNRFppYm5vU0FuSjFLQUFQAQ?hl=ru&gl=RU&ceid=RU%3Aru").text
        sup = BS(response, "html.parser")

        new = sup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")

        for news in new:
            news = news.find("a", class_="DY5T1d RZIKme")
            print(str(x) + ". " + str(news.text))
            print("===")
            sleep(timed)
            x += 1


    def google_world_news(x=1):
        response = requests.get(
            "https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FuSjFHZ0pTVlNnQVAB?hl=ru&gl=RU&ceid=RU%3Aru").text
        sup = BS(response, "html.parser")

        new = sup.find_all("h3", class_="ipQwMb ekueJc RD0gLb")

        for news in new:
            news = news.find("a", class_="DY5T1d RZIKme")
            print(str(x) + ". " + str(news.text))
            print("===")
            sleep(timed)
            x += 1


    def parse_main_page(x=1):
        # Задействуем библиотеку bs4
        soup = BS(request, "html.parser")
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
                sleep(timed)
                x += 1


    def print_smi_news(x=1):
        soup = BS(request, "html.parser")
        url = soup.find("a",
                        class_="home-link2 home-link2_color_blue home-link2_hover_red news__tab news__tab_selected_yes mix-tabber__tab mix-tabber__tab_selected_yes")
        sublink = url.get("href")
        recponce = requests.get(sublink).text
        sup = BS(recponce, "html.parser")
        SMI = sup.find_all("a", class_="mg-card__link")
        for newsmi in SMI:
            newsmi = newsmi.find("h2", class_="mg-card__title")
            print(str(x) + ". " + newsmi.text)
            print("===")
            sleep(timed)
            x += 1


    print("Это парсер. Его функция заключается в нахождении новостей.")

    Wifi = check_wifi()
    che = choise_source_site()
    check_version()

    bol = True

    # Цикл
    while bol:
        if Wifi == True:
            # Выбор пользователя
            if che == "yandex":
                print("Вывести новости с главной страницы 'Яндекс' (1)")
                print("Вывести новости СМИ (2)")
                print("Задать время ожидания (3)")
                print("Очистить (4)")
                print("Переустановить (обновить) программу (5)")
                print("Выход (6)")
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

                elif vr == "4":
                    clear_news()

                elif vr == "5":
                    upgrade_program()

                else:
                    bol = False

            else:
                print("Вывести новости из 'Google' (1)")
                print("Вывести мировые новости (2)")
                print("Задать время ожидания (3)")
                print("Очистить (4)")
                print("Переустановить (обновить) программу (5)")
                print("Выход (6)")
                vr = input(">> ").strip()
                if vr == "1":
                    google_russia_news()

                elif vr == "2":
                    google_world_news()

                elif vr == "3":
                    print("Сколько секунд надо ждать?")
                    print("Нажмите Enter, если хотите вернуться!")
                    sec = input("").strip()
                    if sec != "":
                        sleep_func(sec)
                    else:
                        print("Пропущено!")

                elif vr == "4":
                    clear_news()

                elif vr == "5":
                    upgrade_program()

                else:
                    bol = False

except Exception as Except:
    bol = False
    print("Возникла ошибка при выполнении программы")
    print("Перезапустите программу!")
    print("Ошибка: " + str(Except))
    input()