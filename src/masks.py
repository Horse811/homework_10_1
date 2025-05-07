from logger_config import setup_logger


# Инициализация логгера
logger = setup_logger('masks', 'masks.log')


def get_mask_card_number(card_number: str) -> str:
    logger.info(f"Masking card number: {card_number}")
    """Маскирует номер карты"""
    try:
        if len(card_number) != 16 or not card_number.isdigit():
            logger.error(f"Invalid card number: {card_number}")
            raise ValueError("Номер карты должен содержать 16 цифр")

        masked = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"
        logger.info(f"Card number masked: {masked}")
        return masked
    except Exception as e:
        logger.exception(f"Error masking card number: {str(e)}")
        raise


def get_mask_account_number(account_number: str) -> str:
    """Маскирует номер счета"""
    try:
        if len(account_number) < 4 or not account_number.isdigit():
            logger.error(f"Invalid account number: {account_number}")
            raise ValueError("Номер счета должен содержать минимум 4 цифры")

        masked = f"**{account_number[-4:]}"
        logger.info(f"Account number masked: {masked}")
        return masked
    except Exception as e:
        logger.exception(f"Error masking account number: {str(e)}")
        raise
