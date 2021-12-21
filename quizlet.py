from database import QuizletDataBase
from helpers import get_words_pair
from log import log, print_error


class Quizlet:
    """Класс, реализующий взаимодействие с пользователем"""

    WELCOME_MESSAGE = '''
        Привет, это программа-помощник для изучения английского языка.
        Для того, чтобы записать новые слова, введи 1
        Для того, чтобы проверить свои знания, введи 2
        Для того, чтобы посмотреть весь словарь, введи 3
        Чтобы выйти, нажмите "Enter" при вводе команды
        '''
    CONTEST_MESSAGE =  '''
        Давай проверим твои знания.
        Я буду вывоводить иностранное слово - нужно ввести перевод
        Но для начала, скажи, сколько слов будем проверять?
        '''

    def __init__(self):
        self.db = QuizletDataBase()
        log(self.WELCOME_MESSAGE)

    def menu(self):
        """Основной метод взаимодействия с пользователем"""

        response = input('Введите команду: ')
        try:
            if response == '1':
                self.__add_word()
            elif response == '2':
                self.__contest_mode()
            elif response == '3':
                self.__print_all_dictionary()
            elif response.lower() == 'help':
                self.__print_help()
            else:
                return self.__quit()
            input('Нажмите "Enter", чтобы продолжить...')
        except AssertionError as _err:
            print_error(str(_err))
        log('''
        Введите следующую команду или help для доступных команд
        ''')
        self.menu()

    def __add_word(self):
        """Записываем слова в """
        log('''
        Введите слово на иностранном языке и слово на русском через ":"
        Пример:
        hello : привет
        ''')
        new_words = input()
        eng_word, rus_word = get_words_pair(new_words)

        self.db.set_words_pair_to_dictionary(eng_word, rus_word)

    def __contest_mode(self):
        """Режим контеста"""
        log(self.CONTEST_MESSAGE)

        count = self.__get_count()
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

    def __print_all_dictionary(self):
        """Распечатываем весь словарь"""
        for eng, rus in self.db.select_all():
            print(f'{eng.zfill(39).replace("0", " ")} - {rus}')

    @staticmethod
    def __print_help():
        """Распечатываем подсказку с командами"""
        log('''
        1 - новые слова
        2 - проверить знания
        3 - весь словарь
        ''')

    @staticmethod
    def __quit():
        """Выйти из программы"""
        log('''
        Спасибо за визит, удачи в изучении
        ''')

    @staticmethod
    def __get_count() -> int:
        """Получаем кол-во слов для контеста, дожидаясь числа"""

        while True:
            count = input('Сколько слов проверим? ')
            if count.isdigit() and count != '0':
                break
            print('Введен ноль или не число, попробуем еще раз')
        return int(count)
