"""Модуль для работы с базой данных"""

import sqlite3


class QuizletDataBase:
    """Класс для работы с базой данных quizlet.db"""

    _INSERT_COMMAND = """INSERT INTO Dictionary (foreign_word, rus_word)
                        VALUES ('{}', '{}');"""
    _SELECT_RANDOM_COMMAND = """SELECT foreign_word, rus_word
                               FROM Dictionary ORDER BY RANDOM() LIMIT {}"""
    _SELECT_ALL_COMMAND = "SELECT foreign_word, rus_word FROM Dictionary"
    _DROP_TABLE_COMMAND = "DROP TABLE Dictionary"
    _INIT_TABLE_COMMAND = """
                CREATE TABLE Dictionary(
                id INTEGER PRIMARY KEY,
                foreign_word varchar(50) NOT NULL,
                rus_word varchar(50) NOT NULL);
                """

    def __init__(self):
        """Подключаемся к БД"""

        self._connection = sqlite3.connect(database='quizlet.db')
        self._cursor = self._connection.cursor()

    def __del__(self):
        """Отключаемся от БД"""

        if self._connection:
            self._cursor.close()
            self._connection.close()

    def set_words_pair_to_dictionary(self, foreign_word: str, rus_word: str):
        """
        Добавляем слово на иностранном языке и его перевод в словарь

        :param foreign_word: слово на иностранном языке
        :param rus_word: слово на русском языке
        """

        self._cursor.execute(
            self._INSERT_COMMAND.format(foreign_word, rus_word)
        )
        self._connection.commit()

    def get_random_words(self, count: int):
        """
        Возвращаем слова в случайном порядке

        :param count: Кол-во возвращаемых слов
        :return: Кортеж со строками
        """

        self._cursor.execute(self._SELECT_RANDOM_COMMAND.format(count))
        result = self._cursor.fetchall()
        return result

    def select_all(self):
        """Возвращаем все строки из таблицы"""

        self._cursor.execute(self._SELECT_ALL_COMMAND)
        result = self._cursor.fetchall()
        return result

    # Вспомогательные методы для создания и удаления таблицы

    def init_table(self):
        """Инициализируем таблицу в базе данных"""

        self._cursor.execute(self._INIT_TABLE_COMMAND)
        self._connection.commit()

    def drop_table(self):
        """Удаляем таблицу"""

        self._cursor.execute(self._DROP_TABLE_COMMAND)
        self._connection.commit()
