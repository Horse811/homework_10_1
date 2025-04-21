
import functools
from datetime import datetime


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # Формируем информацию о вызове функции
            func_name = func.__name__
            inputs = f"Inputs: {args}, {kwargs}"

            # Логируем начало выполнения функции
            start_time = datetime.now()
            start_msg = f"{start_time} - {func_name} started with {inputs}\n"

            if filename:
                with open(filename, 'a') as f:
                    f.write(start_msg)
            else:
                print(start_msg, end='')

            try:
                # Выполняем функцию
                result = func(*args, **kwargs)

                # Логируем успешное завершение
                end_time = datetime.now()
                duration = end_time - start_time
                success_msg = f"{end_time} - {func_name} ok. Result: {result}. Duration: {duration}\n"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(success_msg)
                else:
                    print(success_msg, end='')

                return result

            except Exception as e:
                # Логируем ошибку
                end_time = datetime.now()
                duration = end_time - start_time
                error_msg = f"{end_time} - {func_name} error: {type(e).__name__}: {str(e)}. {inputs}. Duration: {duration}\n"

                if filename:
                    with open(filename, 'a') as f:
                        f.write(error_msg)
                else:
                    print(error_msg, end='')

                raise  # Пробрасываем исключение дальше

        return wrapper

    return decorator
