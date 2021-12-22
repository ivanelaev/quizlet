"""Скрипт для заполнения базы данных готовыми значениями"""

import os

from database import QuizletDataBase

with open(os.path.join('database', 'dictionary', 'dictionary_data.txt'),
          'r', encoding='utf-8') as file:
    db = QuizletDataBase()
    db.init_table()
    for line in file:
        foreign_word, rus_word = line.replace('\n', '').split(';')
        db.set_words_pair_to_dictionary(foreign_word, rus_word)
