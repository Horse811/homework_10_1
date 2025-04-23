import pytest

from src.decorators import log


# Вспомогательная функция для чтения файла (если логи пишутся в файл)
def read_log_file(filename):
    with open(filename, 'r') as f:
        return f.read()


# Тест для логирования в консоль (filename=None)
def test_log_to_console(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(2, 3)
    captured = capsys.readouterr()
    output = captured.out

    assert "add started" in output
    assert "add ok" in output
    assert str(result) in output


# Тест для логирования в файл (filename указан)
def test_log_to_file(tmp_path):
    log_file = tmp_path / "test_log.txt"

    @log(filename=str(log_file))
    def multiply(x, y):
        return x * y

    result = multiply(4, 5)
    log_content = read_log_file(log_file)

    assert "multiply started" in log_content
    assert "multiply ok" in log_content
    assert str(result) in log_content


# Тест для проверки логирования ошибок (консоль)
def test_log_error_to_console(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    output = captured.out

    assert "divide started" in output
    assert "ZeroDivisionError" in output
    assert "Inputs: (10, 0)" in output


# Тест для проверки логирования ошибок (файл)
def test_log_error_to_file(tmp_path):
    log_file = tmp_path / "error_log.txt"

    @log(filename=str(log_file))
    def failing_func(x):
        raise ValueError("Oops")

    with pytest.raises(ValueError):
        failing_func(42)

    log_content = read_log_file(log_file)

    assert "failing_func started" in log_content
    assert "ValueError" in log_content
    assert "Inputs: (42,)" in log_content


# Тест для проверки, что декоратор сохраняет имя и docstring функции
def test_decorator_preserves_metadata():
    @log()
    def sample_func():
        """Тестовая функция"""
        pass

    assert sample_func.__name__ == "sample_func"
    assert sample_func.__doc__ == "Тестовая функция"
