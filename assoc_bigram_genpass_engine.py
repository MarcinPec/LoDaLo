import random
import polish_data
from collections import defaultdict


class AsociationalBigramPassGen:
    def __init__(self, length: int, word1: str, word2: str, separate: bool, data_polish: bool):
        self.length = length
        self.word1 = word1
        self.word2 = word2
        self.separate = separate
        self.data_polish = data_polish

    def training_data_load(self):
        if self.data_polish is True:
            polish_words = polish_data.polish_words
            return polish_words
        else:
            data = ['']
            return data

    def bigram_generator(self):
        data = self.training_data_load()
        bigrams = defaultdict(list)
        for word in data:
            for i in range(len(word) - 1):
                bigram = word[i:i+2]
                next_char = word[i+2] if i+2 < len(word) else None
                bigrams[bigram].append(next_char)
        return bigrams

    def generate_password_segment(self, password):
        bigrams = self.bigram_generator()
        while len(password) < int(self.length/2):
            last_bigram = password[-2:]
            next_chars = bigrams.get(last_bigram)
            if not next_chars:
                break
            next_char = random.choice(next_chars)
            if next_char:
                password += next_char
            else:
                break
        return password

    def password_assembler(self):
        password_seg1 = self.generate_password_segment(self.word1)
        password_seg2 = self.generate_password_segment(self.word2)
        if self.separate is True:
            return f'{password_seg1}*{password_seg2}'
        elif self.separate is False:
            return f'{password_seg1}{password_seg2}'

    def __str__(self):
        return f'{self.password_assembler()}'


test = AsociationalBigramPassGen(16, 'Kupa', 'Dom', True, True)
print(test)

