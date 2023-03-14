from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup для разбора html-кода
import requests # импортируем библиотеку requests для выполнения http-запросов

def parse():
    base_url = 'https://www.omgtu.ru/l/' # передаем необходимы URL адрес
    current_url = None
    for page in range(1, 11): # добавим цикл для переключегия страниц 1...10
        current_url = base_url + f"?PAGEN_1={page}" # с помощью f-строки передаём номер страницы
        page = requests.get(current_url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
        print(page.status_code)  # смотрим ответ сервера, чтобы убедиться, что запрос был выполнен
        soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4 в качестве аргументов html-кода и парсер, который будет использоваться для его обработки
        block = soup.findAll('div', class_='news__item') # находим  контейнер с нужным классом
        with open('results.txt', 'a') as f: # создание отдельного файла для записи результата
            for data in block: # проходим циклом по содержимому контейнера
                description = data.find('h3').text.strip() # записываем в переменную содержание тега
                f.write(description + '\n')

