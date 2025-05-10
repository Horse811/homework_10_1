from src.masks import get_mask_card_number

print(get_mask_card_number("0000000000000000"))

import json
import csv
import openpyxl
import re
from typing import List, Dict
from collections import Counter
from operations import (
    filter_transactions_by_description,
    count_transactions_by_category,
)


def load_transactions(filename: str) -> List[Dict]:
    """Загружает транзакции из файла в зависимости от расширения"""
    if filename.endswith('.json'):
        with open(filename, 'r') as f:
            return json.load(f)
    elif filename.endswith('.csv'):
        with open(filename, 'r') as f:
            return list(csv.DictReader(f))
    elif filename.endswith('.xlsx'):
        workbook = openpyxl.load_workbook(filename)
        sheet = workbook.active
        return [
            dict(zip([cell.value for cell in sheet[1]], row))
            for row in sheet.iter_rows(min_row=2, values_only=True)
        ]
    raise ValueError("Unsupported file format")


def main():
    """Основная функция взаимодействия с пользователем"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # Выбор файла
    file_type = input(
        "Выберите тип файла:\n1. JSON\n2. CSV\n3. XLSX\nВаш выбор: "
    ).strip()

    try:
        filename = input("Введите путь к файлу: ").strip()
        transactions = load_transactions(filename)
        print(f"Загружено {len(transactions)} транзакций")
    except Exception as e:
        print(f"Ошибка загрузки файла: {e}")
        return

    # Фильтрация по статусу
    valid_statuses = ["EXECUTED", "CANCELED", "PENDING"]
    while True:
        status = input(
            f"Введите статус ({', '.join(valid_statuses)}): "
        ).upper()
        if status in valid_statuses:
            transactions = [
                t for t in transactions
                if t.get("status", "").upper() == status
            ]
            print(f"Найдено {len(transactions)} транзакций со статусом {status}")
            break
        print("Неверный статус, попробуйте еще раз")

    # Дополнительные фильтры
    if input("Фильтровать по описанию? (да/нет): ").lower() == 'да':
        search = input("Введите текст для поиска: ").strip()
        transactions = filter_transactions_by_description(transactions, search)
        print(f"Найдено {len(transactions)} транзакций с текстом '{search}'")

    # Вывод результатов
    if not transactions:
        print("Нет транзакций, соответствующих критериям")
        return

    for t in transactions[:5]:  # Ограничиваем вывод первыми 5 транзакциями
        print(f"{t.get('date', 'N/A')} {t.get('description', 'No description')}")

    # Статистика по категориям
    if input("Показать статистику по категориям? (да/нет): ").lower() == 'да':
        categories = input("Введите категории через запятую: ").split(',')
        stats = count_transactions_by_category(
            transactions,
            [c.strip() for c in categories if c.strip()]
        )
        for category, count in stats.items():
            print(f"{category}: {count} операций")


if __name__ == "__main__":
    main()
