"""Модуль нужен для заполнения базы данных"""
import os

from database import DataBase

with open(os.path.join('..', 'dictionary', 'dictionary_data.txt'), 'r', encoding='utf-8') as file:
    db = DataBase()
    db.init_table()
    for line in file:
        eng, rus = line.replace('\n', '').split(';')
        db.add_word_definition(eng, rus)
