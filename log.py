def log(text: str):
    """
    Выводит форматированный текст
    :param text: текст
    """
    print_delimiter()
    print(text)
    print_delimiter()


def print_delimiter():
    """Выводит разделитель"""
    print("="*81)
