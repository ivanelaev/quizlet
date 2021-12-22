"""Модуль для логирования и вывода на экран информации пользователю"""

import os
from time import time
from typing import Optional

from helpers import format_log


LOG_FILE_NAME = os.path.join('log', 'logs', f'logs_{int(time())}.txt')


def save_logs(log_function):
    """Декоратор для записи логов в файл"""

    def wrapper(message: str):
        result = log_function(message)
        with open(LOG_FILE_NAME, 'a', encoding='utf-8') as file:
            file.writelines(message)
            if result:
                file.writelines(result)
        return result
    return wrapper


@save_logs
def get_user_input(message: Optional[str] = None) -> Optional[str]:
    """
    Получаем ввод пользователя

    :param message: сообщение, выводимое для пользователя при считвании ответа
    :return: сообщение пользователя
    """
    if message:
        return input(format_log(message))
    return input(' '*8)


@save_logs
def log(message: str):
    """
    Выводим отформатированный текст

    :param message: текст
    """
    print(format_log(message))


@save_logs
def log_text_block(message: str):
    """
    Выводим блок текста

    :param message: текст
    """

    print_delimiter()
    print(message)
    print_delimiter()


def print_delimiter():
    """Выводим разделитель"""

    print("="*81)
