import random as rnd
import string as string
from utility import *


class GenLog:
    def __init__(self, pattern=str, pass_long=int, numbs=bool, letters=bool, special_signs=bool):
        self.pattern = pattern
        self.pass_long = pass_long
        self.numbs = numbs
        self.letters = letters
        self.special_signs = special_signs

    @staticmethod
    @gen_express_list
    def number_gen(length):
        for _ in range(length):
            numbs = str(rnd.randint(0, 9))
            yield numbs

    @staticmethod
    @gen_express_list
    def letter_gen(length):
        for _ in range(length):
            letters = rnd.choice(string.ascii_letters)
            yield letters

    @staticmethod
    @gen_express_list
    def special_signs_gen(length):
        special = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '?', ';']
        for _ in range(length):
            signs = rnd.choice(special)
            yield signs

    @gen_express_str
    def pass_assembler(self):
        pattern_len = len(self.pattern)
        generated_char_numb = self.pass_long - pattern_len
        if generated_char_numb <= 0:
            return self.pattern
        else:
            if self.numbs and self.letters and self.special_signs:
                long1 = rnd.randint(1, generated_char_numb)
                long2 = generated_char_numb - long1
                long3 = generated_char_numb - long1 - long2
                result = self.number_gen(long1) + self.letter_gen(long2) + self.special_signs_gen(long3)
                rnd.shuffle(result)
                result.append(self.pattern)
                return reversed(result)
            elif not self.numbs and not self.letters and not self.special_signs:
                return f'How should I generate this password without any arguments, huh?'
            elif self.numbs and not self.letters and not self.special_signs:
                return self.number_gen(self.pass_long)
            elif self.numbs and not self.letters and self.special_signs:
                long1 = rnd.randint(1, (self.pass_long / 2))
                long2 = 0
                long3 = self.pass_long - long1 - long2
                result = self.number_gen(long1) + self.special_signs_gen(long3)
                rnd.shuffle(result)
                return result
            elif self.numbs and self.letters and not self.special_signs:
                long1 = rnd.randint(1, (int(self.pass_long / 2)))
                long2 = self.pass_long - long1 - 1
                result = self.number_gen(long1) + self.letter_gen(long2)
                rnd.shuffle(result)
                return result
            elif not self.numbs and self.letters and not self.special_signs:
                return self.letter_gen(self.pass_long)
            elif not self.numbs and self.letter_gen and self.special_signs:
                long1 = rnd.randint(1, (int(self.pass_long / 2)))
                long2 = self.pass_long - long1
                result = self.letter_gen(long1) + self.special_signs_gen(long2)
                rnd.shuffle(result)
                return result
            elif not self.numbs and not self.letters and self.special_signs:
                return self.special_signs_gen(self.pass_long)

    def __str__(self):
        return f'{self.pass_assembler()}'


test = GenLog('kurwa', 10, True, True, True)
print(test)
