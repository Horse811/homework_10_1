# Project Bank

Этот проект предоставляет возможность обработки банковских данных, с помощью функций: маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка информации об операциях.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number`: Маскирует номер карты, скрывая часть цифр в середине.
-   `get_mask_account`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card`: Возвращает информацию о карте или счете клиента, маскируя номер.
-   `get_date`: Преобразует системную дату в формат 'ДД.ММ.ГГГГ'.
-   `filter_by_state`: Фильтрует список операций по успешности выполнения, на основе значения ключа `state`.
-   `sort_by_date`: Сортирует список операций по дате, на основе значения ключа 'date'.
-   `filter_by_currency`: Фильтрует список транзакций и возвращает по одной те, что совершены в заданной валюте.
-   `transaction_descriptions`: Обрабатывает список транзакций и поочередно возвращает описание каждой из них.
-   `card_number_generator`: Функция представляет собой генератор номеров банковских карт: создает номера в заданном диапазоне и возвращает их в формате XXXX XXXX XXXX XXXX.
-   `log`: Функция-декоратор, которая фиксирует запуск других функций, передаваемые при запуске аргументы, вычисляет время исполнения, результаты, сообщает сведения об ошибках, если они возникли при выполнении.
Может выводить полученные данные в консоль или записывать в файл.
-   `get_operations`: Позволяет распаковывать данные о транзакциях, содержащиеся в JSON-файле.
-   `get_amount_transaction`: Выводит сумму в рублях по курсу на дату совершения транзакции.
-   `get_transactions_csv`: Считывает из файла в формате .csv список транзакций и возвращает их в виде словаря (dict).
-   `get_transactions_xlsx`: Считывает из файла в формате .xlsx список транзакций и возвращает их в виде словаря (dict).
Точкой входа является файл `main.py`. Он позволяет запустить все функции с использованием классических примеров входных данных.

## Тестирование

Для тестирования работы каждой функции в условиях получения различных входных данных (в том числе, ошибочных и неполных) существует группа тестов в пакете `tests`.
В модуле `conftest.py` содержатся вспомогательные функции (фикстуры), используемые при проведении тестов.

## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git clone git@github.com:OksanaNiklashkova/Bank_Widget.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd project_bank
    ```

3.  **Установите зависимости с помощью Poetry:**

    ```
    poetry install
    ```
4. **Запустите файл main.py, чтобы ознакомиться с примерами работы функций**

    ```
    python main.py
    ```

## Использование

Примеры использования функций:

~~~
from datetime import datetime
from src.widget import get_mask_card_number, get_mask_account, mask_account_card, get_date, filter_by_state, sort_by_date
from typing import List

Маскировка номера карты
card_number = "1234567890123456"
masked_number = get_mask_card_number(card_number)
print(f"Информация о карте: {masked_number}") # Output: 1234 56** **** 3456

Маскировка номера счета
account_number = "12345678901234567890"
masked_account = get_mask_account(account_number)
print(f"Информация о счете: {masked_account}") # Output: **7890

Маскировка информации о карте/счете
input_information = "Visa Classic 1234567890123456"
masked_information = mask_account_card(input_information)
print(f"Информация о карте/счете: {masked_information}") # Output: Visa Classic 1234 56** **** 3456

Преобразование даты
input_date = "2023-03-06T00:00:00"
formated_date = get_date(input_date)
print(f"Дата операции: {formated_date}") # Output: 26.10.2023

Пример данных для фильтрации и сортировки
operations = [
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},
]

Фильтрация по статусу
list_of_operation = filter_by_state(operations, state="EXECUTED")
print(f"Успешные операции: \n{list_of_operation}")

# Output:
[{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},]

Сортировка по дате
sort_by_date_list = sort_by_date(operations)
print(f"Список операций: \n{sort_by_date_list}")

# Output:
[{"id": 2, "date": "2023-10-26T12:00:00", "state": "CANCELED", "amount": 50},
{"id": 1, "date": "2023-10-27T10:00:00", "state": "EXECUTED", "amount": 100},
{"id": 3, "date": "2023-10-28T14:00:00", "state": "EXECUTED", "amount": 200},]


Фильтрация по валюте

Пример входных данных:
transaction_list = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
]

result = filter_by_currency(transaction_list, currency="USD")
print(f"Список транзакций в валюте {currecy}:")
for transaction in result:
    print(transaction)
    
# Output:
{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    }
    
    
Описание типов транзакций

Пример входных данных: аналогично функции "Фильтрация по валюте"
item = transaction_descriptions(transaction_list)
print("Типы транзакций:")
for transaction in item:
    print(transaction)   
# Output:
Перевод организации
Перевод со счета на счет
    
Генератор номеров карт

Пример входных данных:
  start = 1
  stop = 3
  generator = card_number_generator(start, stop)
    for card in generator:
        print(card)  
        
# Output:
0000 0000 0000 0001
0000 0000 0000 0002   

Декоратор @log
Пример для вызова функции:
mask_account_card('Visa Classic 6831982476737658')

# Output:
mask_account_card started with arguments: ('Visa Classic 6831982476737658\n',), {}
Execution time: 0:00:00.000086
mask_account_card ended -> OK
Results: Visa Classic 6831 98** **** 7658   

Чтение операций из файла
Для успешного чтения операций, перечисленных в файле operations.json, расположенном в папке data, вызовите функцию без указания аргумента:
print(get_operations())
Для обращения к определенной транзакции по номеру, укажите "номер+1" в квадратных скобках:
print(get_operations()[2])

# Output:
{
    "id": 939719570,
    "state": "EXECUTED",
    "date": "2018-06-30T02:08:58.425572",
    "operationAmount": {
      "amount": "9824.07",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "Счет 75106830613657916952",
    "to": "Счет 11776614605963066702"
  }

Расчет суммы операции в рублях.
Функция работает с транзакциями, получаемыми из файла operations.json с помощью get_operations().
Можно передавать любые свои данные в виде словаря, имеющего ключи "date", "amount" и "currency"["code"].
Для транзакции из примера выше:

# Output:
Сумма по операции в рублях: 616804.61

Считывание информации о банковских транзакциях из файлов формата .csv и .xlsx.
Функции работают с файлами, расположенными в папке `data`.
Распаковывают данные и возвращают каждую транзакцию в виде словаря Python.

# Output:
 {'id': '650703',
 'state': 'EXECUTED',
 'date': '2023-09-05T11:30:32Z',
 'amount': '16210',
 'currency_name': 'Sol',
 'currency_code': 'PEN',
 'from': 'Счет 58803664561298323391',
 'to': 'Счет 39745660563456619397',
 'description': 'Перевод организации'}
~~~

## Зависимости

Проект использует следующие зависимости:

*   Python 3.13
*   Poetry (для управления зависимостями)


## Лицензия

Этот проект лицензирован по [лицензии MIT](LICENSE).
