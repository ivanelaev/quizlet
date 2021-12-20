import re


class InputFormat:
    """Класс необходим для обработки входящих данных"""

    @staticmethod
    def get_words_pair(input_string:  str) -> tuple:
        """
        Разбивает ответ пользователя на 2 слова
        :param input_string: строка, введеная пользователем
        :return: tuple с двумя строками: иностранное слово и русское слово
        """

        assert ':' in input_string, 'В строке нет разделителя'
        input_string = re.sub(' +', ' ', input_string.replace(':', ' : '))
        first_word, second_word = input_string.split(' : ', 1)
        assert ':' not in second_word, 'В строке несколько символов-разделителей'
        return first_word, second_word

    @staticmethod
    def get_rus_and_foreign_word(words: tuple) -> tuple:
        """
        Определяет русское и иностранное слово
        :param words: пара слов
        :return: tuple с парой в формате (Иностранное слово, Русское слово)
        """
        for index, word in enumerate(words):
            if re.fullmatch(r'[а-я]+[-]*[а-я]+', word.lower()):
                return words[index-1], words[index]
        raise AssertionError('Нет слова на русском языке')
