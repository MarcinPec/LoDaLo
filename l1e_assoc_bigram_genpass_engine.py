import random as rnd
import polish_data
import english_data
from l6_utility import *
from collections import defaultdict


class AsociationalBigramPassGen:
    def __init__(self, word1: str, word2: str, separate: bool, data_polish: bool, data_english: bool):
        self.length = 20
        self.word1 = word1
        self.word2 = word2
        self.separate = separate
        self.data_polish = data_polish
        self.data_english = data_english

    def training_data_load(self):
        polish_words = polish_data.polish_words
        english_words = english_data.english_words
        if self.data_polish and not self.data_english:
            return polish_words
        elif not self.data_polish and self.data_english:
            return english_words
        elif self.data_polish and self.data_english:
            pol_ang = polish_words + english_words
            rnd.shuffle(pol_ang)
            return pol_ang
        else:
            data = ['']
            return data

    def bigram_generator(self):
        data = self.training_data_load()
        bigrams = defaultdict(list)
        for word in data:
            for i in range(len(word) - 1):
                bigram = word[i:i + 2]
                next_char = word[i + 2] if i + 2 < len(word) else None
                bigrams[bigram].append(next_char)
        return bigrams

    def generate_password_segment(self, password):
        bigrams = self.bigram_generator()
        random_bigram = rnd.choice(list(bigrams.keys()))
        next_chars = bigrams[random_bigram]
        if not next_chars:
            return ''
        next_char = rnd.choice(next_chars)
        if next_char:
            password += random_bigram + next_char
        return password

    @staticmethod
    @gen_express_str
    def special_signs_gen():
        special = ['!', '@', '#', '$', '%', '^', '&', '*', '/', '?', ';', ']']
        for _ in range(1):
            sign = rnd.choice(special)
            yield sign

    def password_assembler(self):
        password_seg1 = self.generate_password_segment(self.word1)
        password_seg2 = self.generate_password_segment(self.word2)
        separator = self.special_signs_gen()
        if self.separate:
            return f'{password_seg1}{separator}{password_seg2}'
        elif not self.separate:
            return f'{password_seg1}{password_seg2}'

    def __str__(self):
        return f'{self.password_assembler()}'


