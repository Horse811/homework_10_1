from src.masks import get_mask_card_number

print(get_mask_card_number("0000000000000000"))

import json
import re
from datetime import datetime
from typing import List, Dict, Optional


def load_transactions(filename: str) -> List[Dict]:
    """Загрузка транзакций из JSON-файла"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


def filter_by_status(transactions: List[Dict], status: str) -> List[Dict]:
    """Фильтрация транзакций по статусу"""
    return [t for t in transactions if t.get('status', '').upper() == status.upper()]


def sort_transactions(transactions: List[Dict], reverse: bool = False) -> List[Dict]:
    """Сортировка транзакций по дате"""
    return sorted(
        transactions,
        key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f') if 'date' in x else datetime.min,
        reverse=reverse
    )


def filter_by_currency(transactions: List[Dict], currency: str) -> List[Dict]:
    """Фильтрация транзакций по валюте"""
    currency = currency.lower()
    return [t for t in transactions if t.get('currency', '').lower() == currency]


def format_transaction(transaction: Dict) -> str:
    """Форматирование транзакции для вывода"""
    date = datetime.strptime(transaction['date'], '%Y-%m-%dT%H:%M:%S.%f').strftime('%d.%m.%Y')
    description = transaction.get('description', 'Без описания')

    amount = f"{transaction['amount']} {transaction['currency']}"
    if 'from' in transaction and 'to' in transaction:
        details = f"{transaction['from']} -> {transaction['to']}"
    else:
        details = f"Счет **{transaction.get('to', 'XXXX')[-4:]}"

    return f"{date} {description}\n{details}\nСумма: {amount}\n"


def main():
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Загрузка данных
    try:
        filename = input("Введите имя JSON-файла с транзакциями: ")
        transactions = load_transactions(filename)
        print(f"Загружено {len(transactions)} транзакций")
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return

    # Фильтрация по статусу
    valid_statuses = ['EXECUTED', 'CANCELED', 'PENDING']
    while True:
        status = input(f"Введите статус ({', '.join(valid_statuses)}): ").upper()
        if status in valid_statuses:
            transactions = filter_by_status(transactions, status)
            print(f"Найдено {len(transactions)} транзакций со статусом {status}")
            break
        print("Неверный статус, попробуйте еще раз")

    # Сортировка по дате
    sort_answer = input("Отсортировать по дате? (да/нет): ").lower()
    if sort_answer == 'да':
        order = input("По возрастанию или убыванию? (возр/убыв): ").lower()
        transactions = sort_transactions(transactions, reverse=order == 'убыв')

    # Фильтрация по валюте
    currency_answer = input("Фильтровать по валюте? (да/нет): ").lower()
    if currency_answer == 'да':
        currency = input("Введите валюту (RUB, USD, EUR и т.д.): ").upper()
        transactions = filter_by_currency(transactions, currency)
        print(f"Найдено {len(transactions)} транзакций в валюте {currency}")

    # Вывод результатов
    if not transactions:
        print("Не найдено транзакций по заданным критериям")
        return

    print("\nРезультаты:")
    for transaction in transactions:
        print(format_transaction(transaction))

    print(f"\nВсего операций: {len(transactions)}")


if __name__ == "__main__":
    main()
