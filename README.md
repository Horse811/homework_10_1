# Project Bank

Этот проект предоставляет набор функций для работы с банковскими данными, такими как маскировка номеров карт и счетов, форматирование дат, фильтрация и сортировка данных о транзакциях.

## Описание

Проект состоит из следующих функций:

-   `get_mask_card_number(user_card_number: str) -> str`: Маскирует номер карты, показывая только первые 6 и последние 4 цифры.
-   `get_mask_account(user_account_number: str) -> str`: Маскирует номер счета, показывая только последние 4 цифры.
-   `mask_account_card(user_bank_details: str) -> str`: Обрабатывает информацию о карте или счете клиента и маскирует номер.
-   `get_date(date_string: str) -> str`: Преобразует дату в формат 'ДД.ММ.ГГГГ'.
-   `filter_by_state(list_dict_info: List[Dict], state: str = "EXECUTED") -> List[Dict]`: Фильтрует список словарей на основе указанного параметра `state`.
-   `sort_by_date(list_dict: List[Dict], reverse: bool = True) -> List[Dict]`: Сортирует список словарей на основе ключа 'date'.

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

## Тестирование

Запуск тестов:
```bash
python -m unittest discover -s tests
```

Проверка покрытия:
```bash
pytest --cov=src --cov-report=html
```

Отчет о покрытии будет доступен в `htmlcov/index.html`

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
