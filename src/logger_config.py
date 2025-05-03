import logging
from pathlib import Path


def setup_logger(name: str, log_file: str) -> logging.Logger:
    """
    Настраивает и возвращает логгер с записью в файл

    Args:
        name: Имя логгера (обычно __name__ модуля)
        log_file: Имя файла для логов (например, 'app.log')

    Returns:
        Настроенный объект логгера
    """
    # Создаем папку logs если ее нет
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)

    # Полный путь к файлу лога
    log_path = log_dir / log_file

    # Создаем логгер
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    # Формат записей
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    # Обработчик для записи в файл (перезаписываем при каждом запуске)
    file_handler = logging.FileHandler(log_path, mode='w')
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)

    # Очищаем предыдущие обработчики
    logger.handlers.clear()

    # Добавляем обработчик
    logger.addHandler(file_handler)

    return logger

# Удалите все вызовы функций вне определения setup_logger
# Этот файл должен только определять функцию, но не выполнять код