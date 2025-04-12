from typing import Any, Iterator, List, Dict, Union


def filter_by_currency(
    transactions: List[Dict[str, Any]],
    currency: str
) -> Iterator[Union[Dict[str, Any], str]]:
    """Фильтрует транзакции по валюте и возвращает итератор."""
    if not transactions:
        yield "Отсутствуют данные для обработки"
        return

    if any(
        not isinstance(t.get("operationAmount"), dict) or
        "currency" not in t["operationAmount"]
        for t in transactions
    ):
        yield "Для одной или нескольких транзакций значение валюты не задано"
        return

    filtered = (
        t for t in transactions
        if t.get("operationAmount", {}).get("currency", {}).get("code") == currency
    )

    if not any(filtered):
        yield "В списке отсутствуют транзакции с данной валютой"
        return

    yield from filtered


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """Извлекает описания транзакций."""
    for t in transactions:
        if "description" in t:
            yield t["description"]


# Тестовые данные
transactions = (
    [
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
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {
                "amount": "79114.93",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188"
        },
        {
            "id": 873106923,
            "state": "EXECUTED",
            "date": "2019-03-23T01:09:46.296404",
            "operationAmount": {
                "amount": "43318.34",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод со счета на счет",
            "from": "Счет 44812258784861134719",
            "to": "Счет 74489636417521191160"
        },
        {
            "id": 895315941,
            "state": "EXECUTED",
            "date": "2018-08-19T04:27:37.904916",
            "operationAmount": {
                "amount": "56883.54",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "Visa Classic 6831982476737658",
            "to": "Visa Platinum 8990922113665229"
        },
        {
            "id": 594226727,
            "state": "CANCELED",
            "date": "2018-09-12T21:27:25.241689",
            "operationAmount": {
                "amount": "67314.70",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Visa Platinum 1246377376343588",
            "to": "Счет 14211924144426031657"
        }
    ]
)

# Пример использования filter_by_currency
print("Транзакции в USD:")
usd_transactions = filter_by_currency(transactions, "USD")
for t in usd_transactions:
    print(t)

# Пример использования transaction_descriptions
print("\nОписания транзакций:")
descriptions = transaction_descriptions(transactions)
for desc in descriptions:
    print(desc)


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX.

    Args:
        start: Начальное значение номера карты
        stop: Конечное значение (не включается)

    Yields:
        Номера карт в заданном диапазоне

    Raises:
        TypeError: Если аргументы не целые числа
        ValueError: При некорректных значениях границ диапазона
    """
    if not isinstance(start, int) or not isinstance(stop, int):
        raise TypeError("Неверный формат данных!")

    if start <= 0 or len(str(start)) > 16 or len(str(stop)) > 16:
        raise ValueError("Ошибка при вводе значений границ диапазона!")

    if start >= stop:
        raise ValueError("Ошибка: начальное значение должно быть меньше конечного!")

    current = start
    while current != stop:
        zero_count = 16 - len(str(current))
        result = "0" * zero_count + str(current)
        card_number = f"{result[:4]} {result[4:8]} {result[8:12]} {result[12:]}"
        yield card_number
        current += 1


try:
    start = 1
    stop = 6

    generator = card_number_generator(start, stop)
    for card in generator:
        print(card)

except (TypeError, ValueError) as e:
    print(e)
