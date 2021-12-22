"""Модуль для обработки строковых переменных"""

import re

# Регулярное выражение для проверки того, что слово на русском языке
RUS_RE = r'[а-я]+[-]*[а-я]+'


def get_words_pair(input_string:  str) -> tuple:
    """
    Проверяем введеные значения и разбиваем на пару

    :param input_string: строка, введеная пользователем
    :return: tuple с двумя строками: иностранное слово и русское слово
    """

    # Удаляем лишние пробелы.
    # Разбиваем строку с помощью раздилителя.
    # Проверяем, что в строке два слова.
    assert ':' in input_string, 'В строке нет разделителя'
    input_string = re.sub(' +', ' ', input_string.replace(':', ' : '))
    words = input_string.split(' : ')
    assert len(words) == 2, 'В строке несколько символов-разделителей'

    # Проверяем, что одно из слов написано на русском языке,
    # а второе слово не на русском
    for index, word in enumerate(words):
        if re.fullmatch(RUS_RE, word.lower()):
            assert re.fullmatch(RUS_RE, words[index-1].lower()) is None
            return words[index-1], words[index]

    raise AssertionError('Нет слова на русском языке')


def format_log(message: str) -> str:
    """
    Форматируем сообщение, для логов, добавляем в начале
    отступ в 8 пробелов для красоты

    :param message: сообщение
    :return: отформатированное сообщение
    """
    return ''.join(['\n', ' '*8, re.sub(' +', ' ', message)])
