from database import DataBase
from helpers import InputFormat
from log import log, print_error


class Quizlet:
    def __init__(self):
        self.db = DataBase()
        log('''
        Привет, это программа-помощник для изучения английского языка.
        Для того, чтобы записать новые слова, введи 1
        Для того, чтобы проверить свои знания, введи 2
        Для того, чтобы посмотреть весь словарь, введи 3
        Чтобы выйти, нажмите "Enter" при вводе команды
        ''')
        self.menu()

    def menu(self):
        """Обработать ответ"""
        response = input('Введите команду: ')
        try:
            if response == '1':
                self.add_word()
            elif response == '2':
                self.contest_mode()
            elif response == '3':
                self.print_all_dictionary()
            elif response.lower() == 'help':
                self.print_help()
            else:
                return self.quit()
            input('Нажмите "Enter", чтобы продолжить...')
        except AssertionError as _err:
            print_error(str(_err))
        log('''
        Введите следующую команду или help для доступных команд
        ''')
        self.menu()

    def add_word(self):
        """Добавление слова"""
        log('''
        Введите слово на иностранном языке и слово на русском через ":"
        Пример:
        hello : привет
        ''')
        new_words = input()
        words_pair = InputFormat.get_words_pair(new_words)
        eng_word, rus_word = InputFormat.get_rus_and_foreign_word(words_pair)

        self.db.add_word_definition(eng_word, rus_word)

    def contest_mode(self):
        """Режим контеста"""
        log('''
        Давай проверим твои знания.
        Я буду вывоводить иностранное слово - нужно ввести перевод
        Но для начала, скажи, сколько слов будем проверять?
        ''')

        count = self.get_count()
        result = 0
        words_pair = self.db.get_random_words(count)
        for eng, rus in words_pair:
            response = input(f'''
            {eng} - ''')
            if response == rus:
                print('\nПравильно, идём дальше\n')
                result += 1
            else:
                print('\nНеправильно, идём дальше\n')
        log(f'Правильно отвечено {result} из {len(words_pair)} слов')

    def print_all_dictionary(self):
        """Распечатываем весь словарь"""
        for eng, rus in self.db.select_all():
            print(f'{eng.zfill(39).replace("0", " ")} - {rus}')

    @staticmethod
    def print_help():
        """Распечатываем подсказку с командами"""
        log('''
        1 - новые слова
        2 - проверить знания
        3 - весь словарь
        ''')

    @staticmethod
    def quit():
        """Выйти из программы"""
        log('''
        Спасибо за визит, удачи в изучении
        ''')

    @staticmethod
    def get_count() -> int:
        """Получаем кол-во слов для контеста, дожидаясь числа"""

        while True:
            count = input('Сколько слов проверим? ')
            if count.isdigit() and count != '0':
                break
            print('Введен ноль или не число, попробуем еще раз')
        return int(count)
