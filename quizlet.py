from database import DataBase
from log import log


class Quizlet:
    def __init__(self):
        self.db = DataBase()
        log('''
        Привет, это программа-помощник для изучения английского языка.
        Для того, чтобы записать новые слова, введи 1
        Для того, чтобы проверить свои знания, введи 2
        Для того, чтобы посмотреть весь словарь, введи 3
        ''')
        self.menu()

    def menu(self):
        """Обработать ответ"""
        response = input()
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
        log('''
        Введите следующую команду или help для доступных команд
        ''')
        self.menu()

    def add_word(self):
        """Добавление слова"""
        log('''
        Введите слово на английском и слово на русском через ;
        Пример:
        hello;привет
        ''')
        new_words = input()
        eng_word, rus_word = new_words.split(';')
        self.db.add_word_definition(eng_word, rus_word)

    def contest_mode(self):
        """Режим контеста"""
        log('''
        Давай проверим твои знания.
        Я вывожу иностранное слово - вам нужно ввести перевод
        ''')

        for eng, rus in self.db.get_random_words(10):
            response = input(f'''
            {eng} - ''')
            if response == rus:
                print('Правильно, идём дальше\n')
            else:
                print('Неправильно, идём дальше\n')

    def print_all_dictionary(self):
        """Распечатываем весь словарь"""
        for eng, rus in self.db.select_all():
            print(f'{eng.zfill(39).replace("0", " ")} - {rus}')

    def print_help(self):
        """Распечатываем подсказку с командами"""
        log('''
        1 - новые слова
        2 - проверить знания
        3 - весь словарь
        ''')

    def quit(self):
        """Выйти из программы"""
        log('''
        Спасибо за визит, удачи в изучении
        ''')