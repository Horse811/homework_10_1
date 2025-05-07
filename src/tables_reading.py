import csv
import os
from typing import Any

import pandas as pd


def get_transactions_csv(file_path: str | None = None) -> Any:
    """Функция считывает транзакции из файла .csv и возвращает список словарей"""
    if not file_path:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, "..", "data", "transactions.csv")

    try:
        data_csv = []
        with open(file_path, "r", encoding="UTF-8") as file_csv:
            reader = csv.DictReader(file_csv, delimiter=";")
            for row in reader:
                data_csv.append(row)
            if len(data_csv) != 0:
                return data_csv
            else:
                print("Данные имеют неверный формат!")

    except FileNotFoundError:
        print("Ошибка! Файл не найден!")


def get_transactions_xlsx(file_path: str | None = None) -> Any:
    """Функция считывает транзакции из файла .xlsx и возвращает список словарей"""
    if not file_path:
        file_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(file_dir, "..", "data", "transactions_excel.xlsx")

    try:
        data_frame = pd.read_excel(file_path)
        data_xlsx = data_frame.to_dict(orient="records")
        return data_xlsx
    except FileNotFoundError:
        print("Ошибка! Файл не найден!")
    except Exception:
        print("Данные имеют неверный формат!")


if __name__ == "__main__":
    x = get_transactions_csv()
    print(x[0])
    y = get_transactions_xlsx()
    print(y[0])