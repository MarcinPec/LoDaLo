import torch.nn as nn
import math


class PasswordStrengthModel(nn.Module):
    def __init__(self, password):
        super(PasswordStrengthModel, self).__init__()
        self.password = password

        # Warstwa oceniająca siłę hasła
        self.strength_layer = nn.Sequential(
            nn.Linear(2, 64),
            nn.ReLU(),
            nn.Linear(64, 1),
            nn.Sigmoid()
        )

        # Parametry czasowe do oceny czasu złamania hasła
        self.time_params = {
            'lowercase_letters': 26,
            'uppercase_letters': 26,
            'digits': 10,
            'special_characters': 33,  # np. !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
            'password_length': 8,       # Długość hasła
            'attempts_per_second': 1e6  # Przybliżona liczba prób ataku na sekundę
        }

    def forward(self, x):
        strength = self.strength_layer(x)
        return strength

    def complexity(self):
        charset_size = len(set(self.password))  # Liczba unikalnych znaków w haśle
        password_length = len(self.password)  # Długość hasła
        entropy = math.log2(charset_size) * password_length
        return entropy

    def estimate_cracking_time(self):
        # Obliczenie czasu złamania hasła metodą bruteforce
        complexity = self.complexity()
        password_len = len(self.password)
        charset_size = self.time_params['lowercase_letters'] + \
                       self.time_params['uppercase_letters'] + \
                       self.time_params['digits'] + \
                       self.time_params['special_characters']
        password_space = charset_size ** password_len
        time_to_crack = password_space / self.time_params['attempts_per_second']
        return int(time_to_crack/60) # in minutes

    def __str__(self):
        return f'{self.estimate_cracking_time()}'


