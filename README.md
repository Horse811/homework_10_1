# Project Bank

Этот проект предоставляет набор функций для работы с банковскими данными, такими как маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка данных о транзакциях.

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
Точкой входа является файл `main.py`. Он позволяет запустить все функции с использованием классических примеров входных данных.


## Установка

Для установки и запуска проекта необходимо выполнить следующие шаги:

1.  **Клонируйте репозиторий:**

    ```
    git@github.com:Horse811/homework_10_1.git
    ```

2.  **Перейдите в папку проекта:**

    ```
    cd Home_work
    ```

3.  **Установите зависимости:**

    ```
    pip install -r requirements.txt
    ```
# Banking Data Processing Toolkit



## Модули

### 1. masks.py
Функции для маскирования конфиденциальных данных:

```python
from src.masks import get_mask_card_number, get_mask_account

# Маскирование номера карты (16 цифр)
print(get_mask_card_number("1234567890123456"))  # "1234 56** **** 3456"

# Маскирование номера счета (минимум 4 цифры)
print(get_mask_account("12345678"))  # "**5678"
```

### 2. processing.py
Обработка списка операций:

```python
from src.processing import filter_by_state, sort_by_date

operations = [
    {"id": 1, "state": "EXECUTED", "date": "2023-12-31T23:59:59.999"},
    {"id": 2, "state": "PENDING", "date": "2022-01-01T00:00:00.000"}
]

# Фильтрация по статусу
filtered = filter_by_state(operations, "EXECUTED")

# Сортировка по дате (по умолчанию - новейшие сначала)
sorted_ops = sort_by_date(operations)
```

### 3. widget.py
Утилиты преобразования данных:

```python
from src.widget import mask_account_card, get_date

# Автоматическое маскирование (карта или счет)
print(mask_account_card("1234567890123456"))  # "1234 56** **** 3456"
print(mask_account_card("12345678"))          # "**5678"

# Преобразование даты
print(get_date("2023-12-31T23:59:59.999"))  # "31.12.2023"
```
### 4. generators.py
# Пример 1: Генерация 3 номеров карт

start = 1

stop = 3

generator = card_number_generator(start, stop)

for card in generator:

    print(card) 
        
# Output:
0000 0000 0000 0001

0000 0000 0000 0002

0000 0000 0000 0003

## 🧪 Тестирование

### Структура тестов
```
tests/
├── test_masks.py       # Тесты масок карт/счетов (5 тестов)
├── test_processing.py  # Тесты обработки операций (5 тестов)
├── test_widget.py      # Тесты виджетов (5 тестов)
└── test_generators.py  # Тесты генераторов 
```

### Ключевые особенности:
1. **Фикстуры** через `setUp()`
   ```python
   def setUp(self):
       self.test_data = [...]  # Общие данные для всех тестов класса
   ```

2. **Параметризация** тестов:
   ```python
   @parameterized.expand([
       ("Описание случая", input, expected),
       ...
   ])
   ```

3. **Проверка исключений**:
   ```python
   with self.assertRaises(ValueError) as context:
       function(input)
   self.assertIn("ожидаемое сообщение", str(context.exception))
   ```

### Запуск тестов
```bash
# Все тесты с отчетом о покрытии
pytest --cov=src --cov-report=term-missing

# Генерация HTML-отчета
pytest --cov=src --cov-report=html && open htmlcov/index.html

# Конкретный тестовый класс
python -m unittest tests/test_processing.py
```

**Требования**:
```bash
pip install pytest pytest-cov parameterized
```
## Примеры использования

1. Маскирование данных:
```python
from src.widget import mask_account_card

card_number = "1234567890123456"
account_number = "12345678"

print(f"Card: {mask_account_card(card_number)}")
print(f"Account: {mask_account_card(account_number)}")
```

2. Обработка операций:
```python
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date

operations = [...]  # список операций

# Получить выполненные операции, отсортированные по дате
processed = sort_by_date(
    filter_by_state(operations, "EXECUTED")
)

for op in processed:
    print(f"{get_date(op['date'])} - {op['amount']} {op['currency']}")
```

## Ограничения

- Номер карты должен содержать ровно 16 цифр
- Номер счета должен содержать минимум 4 цифры
- Дата должна быть в формате ISO 8601 (YYYY-MM-DDThh:mm:ss.sss)

## Лицензия

MIT License
