import json
from pathlib import Path
from typing import List, Dict
from logger_config import setup_logger

# Инициализация логгера
logger = setup_logger('utils', 'utils.log')


def load_transactions(file_path: str) -> List[Dict]:
    logger.info(f"Loading transactions from {file_path}")
    """Загружает транзакции из JSON-файла"""
    try:
        path = Path(file_path)

        if not path.exists():
            logger.error(f"File not found: {file_path}")
            return []

        if path.stat().st_size == 0:
            logger.warning(f"Empty file: {file_path}")
            return []

        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)

        if not isinstance(data, list):
            logger.error(f"File does not contain a list: {file_path}")
            return []

        logger.info(f"Successfully loaded {len(data)} transactions from {file_path}")
        return data

    except json.JSONDecodeError as e:
        logger.error(f"Invalid JSON in file {file_path}: {str(e)}")
        return []
    except PermissionError as e:
        logger.error(f"Permission denied for file {file_path}: {str(e)}")
        return []
    except Exception as e:
        logger.exception(f"Unexpected error loading {file_path}: {str(e)}")
        return []
