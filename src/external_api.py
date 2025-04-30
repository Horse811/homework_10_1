import os
import requests
from typing import Dict

from src.generators import transactions

# Инициализация функции load_dotenv
try:
    from dotenv import load_dotenv
except ImportError:
    def load_dotenv():
        pass  # Заглушка, если python-dotenv не установлен

# Загружаем переменные окружения
load_dotenv()

_API_KEY = os.getenv('EXCHANGE_RATES_API_KEY')
_BASE_URL = 'https://api.apilayer.com/exchangerates_data/latest'
_TIMEOUT = 10


def convert_to_rub(transaction: Dict) -> float:
    """Convert transaction amount to RUB.

    Args:
        transaction: Dictionary with 'amount' and 'currency' keys

    Returns:
        Amount in RUB as float

    Raises:
        ValueError: If conversion fails or invalid data provided
    """


    try:
        # Проверка и преобразование суммы
        try:
            amount = float(transaction.get("operationAmount")['amount'])
            currency = transaction.get("operationAmount")['currency']["code"]
        except (KeyError, ValueError, AttributeError) as e:
            raise ValueError(f'Invalid transaction data: {str(e)}') from e

        if currency == 'RUB':
            return amount

        # Запрос к API
        try:
            URL=f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={currency}&amount={amount}'

            response = requests.get(URL, headers={"apikey": _API_KEY})
            response.raise_for_status()
            rate = response.json()['result']
            return round(rate, 2)

        except requests.RequestException as e:
            raise ValueError(f'API request failed: {str(e)}') from e
        except (KeyError, ValueError) as e:
            raise ValueError(f'Invalid API response: {str(e)}') from e

    except Exception as e:
        raise ValueError(f'Conversion failed: {str(e)}') from e
transactions = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    }}
print(convert_to_rub(transactions))
