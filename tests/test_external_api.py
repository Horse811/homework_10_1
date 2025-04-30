import pytest
from unittest.mock import patch, Mock
import requests
from src.external_api import convert_to_rub


@pytest.fixture
def rub_transaction():
    return {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "RUB"}
        }
    }


@pytest.fixture
def usd_transaction():
    return {
        "operationAmount": {
            "amount": "100.00",
            "currency": {"code": "USD"}
        }
    }


@pytest.fixture
def eur_transaction():
    return {
        "operationAmount": {
            "amount": "50.00",
            "currency": {"code": "EUR"}
        }
    }


@pytest.fixture
def invalid_transaction_missing_amount():
    return {
        "operationAmount": {
            "currency": {"code": "USD"}
        }
    }


@pytest.fixture
def invalid_transaction_missing_currency():
    return {
        "operationAmount": {
            "amount": "100.00"
        }
    }


@pytest.fixture
def invalid_transaction_bad_amount():
    return {
        "operationAmount": {
            "amount": "not_a_number",
            "currency": {"code": "USD"}
        }
    }


class TestConvertToRub:
    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    def test_convert_rub_returns_same_amount(self, rub_transaction):
        """Should return same amount for RUB transactions"""
        assert convert_to_rub(rub_transaction) == 1000.00

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    @patch('requests.get')
    def test_convert_usd_success(self, mock_get, usd_transaction):
        """Should convert USD to RUB using API"""
        mock_response = Mock()
        mock_response.json.return_value = {"result": 7500.00}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = convert_to_rub(usd_transaction)

        assert result == 7500.00
        mock_get.assert_called_once_with(
            'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=100.00',
            headers={'apikey': 'test_key'}
        )

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    @patch('requests.get')
    def test_convert_eur_success(self, mock_get, eur_transaction):
        """Should convert EUR to RUB using API"""
        mock_response = Mock()
        mock_response.json.return_value = {"result": 4500.00}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = convert_to_rub(eur_transaction)
        assert result == 4500.00

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    @patch('requests.get')
    def test_convert_api_error(self, mock_get, usd_transaction):
        """Should handle API request errors"""
        mock_get.side_effect = requests.exceptions.RequestException("API error")

        with pytest.raises(ValueError, match="API request failed"):
            convert_to_rub(usd_transaction)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    @patch('requests.get')
    def test_convert_invalid_api_response(self, mock_get, usd_transaction):
        """Should handle invalid API response"""
        mock_response = Mock()
        mock_response.json.return_value = {}  # Missing 'result' field
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        with pytest.raises(ValueError, match="Invalid API response"):
            convert_to_rub(usd_transaction)

    def test_convert_missing_api_key(self, usd_transaction):
        """Should raise error when API key is missing"""
        with pytest.raises(ValueError, match="API key not configured"):
            convert_to_rub(usd_transaction)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    def test_convert_missing_amount(self, invalid_transaction_missing_amount):
        """Should raise error when amount is missing"""
        with pytest.raises(ValueError, match="Invalid transaction data"):
            convert_to_rub(invalid_transaction_missing_amount)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    def test_convert_missing_currency(self, invalid_transaction_missing_currency):
        """Should raise error when currency is missing"""
        with pytest.raises(ValueError, match="Invalid transaction data"):
            convert_to_rub(invalid_transaction_missing_currency)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    def test_convert_invalid_amount(self, invalid_transaction_bad_amount):
        """Should raise error for non-numeric amount"""
        with pytest.raises(ValueError, match="Invalid transaction data"):
            convert_to_rub(invalid_transaction_bad_amount)

    @patch.dict('os.environ', {'EXCHANGE_RATES_API_KEY': 'test_key'}, clear=True)
    @patch('requests.get')
    def test_convert_rounds_result(self, mock_get, usd_transaction):
        """Should round result to 2 decimal places"""
        mock_response = Mock()
        mock_response.json.return_value = {"result": 7500.12345}
        mock_response.raise_for_status.return_value = None
        mock_get.return_value = mock_response

        result = convert_to_rub(usd_transaction)
        assert result == 7500.12
