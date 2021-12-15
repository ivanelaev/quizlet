import re
import sqlite3
from .config import *


class DataBase:

    def __init__(self):
        self.connection = sqlite3.connect(database=db_name)
        print('database connected')

    def __del__(self):
        if self.connection:
            self.connection.close()
        print('database connection closed')

    def add_word_definition(self, eng_word: str, rus_word: str):
        """Добавляет слово и его перевод в словарь"""
        try:
            assert re.match(r'[a-z]*', eng_word.lower()), 'Первое слово должно быть на английском языке'
            assert re.match(r'[а-я]*', rus_word.lower()), 'Второе слово должно быть на русском языке'
        except Exception as _ex:
            return _ex
        cursor = self.connection.cursor()
        cursor.execute(
            f"""INSERT INTO Dictionary (eng_word, rus_word) VALUES
                ('{eng_word}', '{rus_word}');"""
        )
        self.connection.commit()
        cursor.close()

    def get_random_words(self, count: int):
        """
        Возвращает слова в случайном порядке
        :param count: Кол-во возвращаемых слов
        :return: Кортеж со строками
        """
        cursor = self.connection.cursor()
        cursor.execute(f"""
        SELECT eng_word, rus_word FROM Dictionary ORDER BY RANDOM() LIMIT {count}
        """)
        result = cursor.fetchall()
        cursor.close()
        return result

    def select_all(self):
        """Выбирает все строки из таблицы"""
        cursor = self.connection.cursor()
        cursor.execute(""" SELECT eng_word, rus_word FROM Dictionary """)
        result = cursor.fetchall()
        cursor.close()
        return result

    def init_table(self):
        """Инициализирует таблицу в базе данных"""
        cursor = self.connection.cursor()
        cursor.execute(
            """ CREATE TABLE Dictionary(
                id INTEGER PRIMARY KEY,
                eng_word varchar(50) NOT NULL,
                rus_word varchar(50) NOT NULL);"""
        )
        self.connection.commit()
        cursor.close()
        print('Table created')

    def drop_table(self):
        """Снести таблицу"""
        cursor = self.connection.cursor()
        cursor.execute(
            """DROP TABLE Dictionary"""
        )
        self.connection.commit()

        cursor.close()