"""Основной модуль, реализующий логику приложения"""

from log import log, log_text_block, get_user_input
from quizlet import Quizlet


WELCOME_MESSAGE = """
        Привет, это программа-помощник для изучения английского языка.
"""
QUIT_MESSAGE = """
        Спасибо за визит, удачи в изучении
"""


def start_app():
    """Запускаем приложение"""

    log_text_block(WELCOME_MESSAGE)
    quizlet = Quizlet()

    while True:
        quizlet.print_menu()
        response = get_user_input('Введите команду: ')
        try:
            if response == '1':
                quizlet.add_word()
            elif response == '2':
                quizlet.contest_mode()
            elif response == '3':
                quizlet.print_all_dictionary()
            else:
                break
            get_user_input('Нажмите "Enter", чтобы вернуться в меню')
        except AssertionError as _err:
            log(str(_err))

    log_text_block(QUIT_MESSAGE)


if __name__ == '__main__':
    start_app()
