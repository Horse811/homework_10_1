import json
from pathlib import Path
from typing import List, Dict


def load_transactions(file_path: str) -> List[Dict]:
    """Load transactions from JSON file.

    Args:
        file_path: Path to JSON file with transactions data

    Returns:
        List of transactions as dictionaries or empty list if:
        - File not found
        - File is empty
        - File contains invalid JSON
        - JSON content is not a list
    """
    try:
        path = Path(file_path)

        if not path.exists() or path.stat().st_size == 0:
            return []

        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        return data if isinstance(data, list) else []

    except (json.JSONDecodeError, PermissionError):
        return []
