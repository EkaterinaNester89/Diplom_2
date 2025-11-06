# Develop2 Финальный проект Автотесты API


В проекте зайдествованы автотесты для проверки сервиса Stellar burgers с помощью Requests, Pytest и Allure.

## Установка и запуск

Установка зависимостей:

`pip install -r requirements.txt`

Запуск тестов:

`pytest -v`


Запуск автотестов и создание отчета о тестировании в Allure:

`pytest --alluredir=allure_results`

Показ отчета из результатов тестов:

`allure serve ./allure_results`

Генерация отчета из результатов тестов:

`allure generate ./allure_results/ -o allure_report `


## Структура проекта

- Sprint_7/
  - allure_report/ # сгенерированный отчет
  - allure_results/ # сгенерированные файлы до отчета
  - data/ # данные для использования в тестах
  - helpers/ # классы c действиями для разных ручек
  - tests/  # Тесты, сгруппированные по функционалу
  - pytest.ini # настройки pytest 
  - README.md # Текущий файл
  - requirements.txt # Зависимости проекта

  

Автор: Нестер Екатерина Васильевна
https://github.com/EkaterinaNester89/