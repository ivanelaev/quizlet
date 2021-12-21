def log(text: str):
    """
    Выводим форматированный текст

    :param text: текст
    """

    print_delimiter()
    print(text)
    print_delimiter()


def print_error(error_text: str):
    """
    Выводим ошибку

    :param error_text: текст ошибки
    """

    print(f'[ERROR] {error_text}')
    input('Нажмите "Enter", чтобы продолжить...')


def print_delimiter():
    """Выводит разделитель"""

    print("="*81)
