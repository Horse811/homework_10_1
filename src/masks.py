def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер карты (формат: XXXX XX** **** XXXX)."""
    if not card_number or len(card_number) != 16 or not card_number.isdigit():
        raise ValueError("Некорректный номер карты. Должно быть 16 цифр.")
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"

def get_mask_account(account_number: str) -> str:
    """Маскирует номер счёта (формат: **XXXX)."""
    if not account_number or len(account_number) < 4 or not account_number.isdigit():
        raise ValueError("Номер счета должен содержать минимум 4 цифры")
    return f"**{account_number[-4:]}"
