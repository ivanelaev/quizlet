"""Модуль содержит класс для обработки команд пользователя"""

from typing import Optional

from database import QuizletDataBase
from helpers import get_words_pair
from log import log, log_text_block, get_user_input


class Quizlet:
    """Класс, выполняющий команды пользователя"""

    _MENU_MESSAGE = """
        Для того, чтобы записать новые слова, введи 1
        Для того, чтобы проверить свои знания, введи 2
        Для того, чтобы посмотреть весь словарь, введи 3
        Чтобы выйти, нажмите "Enter" при вводе команды
        """
    _CONTEST_MESSAGE = """
        Давай проверим твои знания.
        Я буду вывоводить иностранное слово - нужно ввести перевод
        Но для начала, скажи, сколько слов будем проверять?
        """
    _ADD_WORD_MESSAGE = """
        Введите пару слов на иностранном языке и на русском разделенных ":"
        Пример:
        "hello : привет" или "привет : hello"
        """
    _BACK_TO_MENU_MESSAGE = """
        Чтобы вернуться в меню нажмите "Enter"
        """

    def __init__(self):
        self._data_base = QuizletDataBase()

    def add_word(self):
        """Записываем слова в словарь"""

        log_text_block(self._ADD_WORD_MESSAGE + self._BACK_TO_MENU_MESSAGE)
        new_words = get_user_input('Введите пару слов: ')
        if new_words:
            eng_word, rus_word = get_words_pair(new_words)
            self._data_base.set_words_pair_to_dictionary(eng_word, rus_word)

    def contest_mode(self):
        """Режим контеста"""

        log_text_block(self._CONTEST_MESSAGE + self._BACK_TO_MENU_MESSAGE)
        count = self.__get_count()
        if count is None:  # Обрабатываем пустой ввод
            return
        word_pairs = self._data_base.get_random_words(count)
        result = self.__check_knowledge(word_pairs)
        log(f'Правильно отвечено {result} из {len(word_pairs)} слов')

    def print_all_dictionary(self):
        """Распечатываем весь словарь"""

        for eng, rus in self._data_base.select_all():
            print(f'{eng.zfill(39).replace("0", " ")} - {rus}')

    def print_menu(self):
        """Распечатываем меню"""

        log_text_block(self._MENU_MESSAGE)

    @staticmethod
    def __get_count() -> Optional[int]:
        """Получаем кол-во слов для контеста, дожидаясь числа"""

        while True:
            count = get_user_input('Сколько слов проверим? ')
            if count:  # Обрабатываем пустой ввод
                if count.isdigit() and count != '0':
                    break
                log('Введен ноль или не число, попробуем еще раз')
            else:
                return None
        return int(count)

    @staticmethod
    def __check_knowledge(word_pairs) -> int:
        """
        Проверяем знания пользователя

        :param word_pairs:
        :return:
        """

        result = 0
        for eng, rus in word_pairs:
            response = get_user_input(f"{eng} - ")
            if response == rus:
                log('Правильно, идём дальше')
                result += 1
            else:
                log('Неправильно, идём дальше')
        return result
