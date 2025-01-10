import requests
from bs4 import BeautifulSoup

# Делаем GET-запрос на сайт
url = "https://urban-university.ru/"  # Указываем URL сайта
response = requests.get(url)

#  Проверяем успешность запроса
if response.status_code == 200:
    print(f"Успешный запрос на {url}")

    # Парсинг HTML-контент страницы
    soup = BeautifulSoup(response.text, 'html.parser')

    # Извлекаем заголовки
    headers = soup.find_all(['h1', 'h2', 'h3'])

    # Выводим заголовки на экран
    print("\nЗаголовки на странице:")
    for header in headers:
        print(header.get_text())
else:
    print(f"Ошибка при запросе: {response.status_code}")

