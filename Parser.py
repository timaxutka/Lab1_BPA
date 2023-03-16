from bs4 import BeautifulSoup # импортируем библиотеку BeautifulSoup для разбора html-кода
import requests # импортируем библиотеку requests для выполнения http-запросов

def parse():
    base_url = 'https://www.omgtu.ru/l/?SHOWALL_1=1' # передаем необходимы URL адрес
    page = requests.get(base_url) # отправляем запрос методом Get на данный адрес и получаем ответ в переменную
    print(page.status_code)  # смотрим ответ сервера, чтобы убедиться, что запрос был выполнен
    soup = BeautifulSoup(page.text, "html.parser") # передаем страницу в bs4 в качестве аргументов html-кода и парсер, который будет использоваться для его обработки
    block = soup.findAll('div', class_='news__item') # находим  контейнер с нужным классом
    with open('results.txt', 'a', encoding='utf-8') as f: # создание отдельного файла для записи результата
        for data in block: # проходим циклом по содержимому контейнера
            description = data.find('h3').text.strip() # записываем в переменную содержание тега
            f.write(description + '\n')

