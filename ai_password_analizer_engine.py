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

    def estimate_cracking_time(self):
        # Obliczenie czasu złamania hasła metodą bruteforce
        password_len = len(self.password)
        charset_size = self.time_params['lowercase_letters'] + \
                       self.time_params['uppercase_letters'] + \
                       self.time_params['digits'] + \
                       self.time_params['special_characters']
        password_space = charset_size ** password_len
        time_to_crack = password_space / self.time_params['attempts_per_second']
        return int(time_to_crack) # in seconds

    def __str__(self):
        return f'{self.estimate_cracking_time()}'


class PasswordStrenghtTimer(PasswordStrengthModel):
    def __init__(self, password):
        super().__init__(password)

    def timer_adjuster(self):
        try:
            obj = PasswordStrengthModel(self.password)
            obj_time = obj.estimate_cracking_time()
            min = obj_time/60
            hour = obj_time/3600
            day = obj_time/86400
            month = obj_time/2592000
            year = obj_time/31104000
            thousand_yr = obj_time/31104000000
            million_yr = obj_time/31104000000000
            billion_yr = obj_time/31104000000000000
            trillion_yr = obj_time/31104000000000000000
            quadrillion_yr = obj_time/31104000000000000000000
            if obj_time >31104000000000000000000:
                return f'Inifinity...'
            elif 31104000000000000000000 > obj_time >31104000000000000000:
                return f'{round(trillion_yr, 1)} trillion years'
            elif 31104000000000000000 > obj_time > 31104000000000000:
                return f'{round(billion_yr, 1)} billion years'
            elif 31104000000000000 > obj_time >= 31104000000000:
                return f'{round(million_yr, 1)} million years'
            elif 31104000000000 > obj_time >= 31104000000:
                return f'{round(thousand_yr, 1)} thousand years'
            elif 31104000000 > obj_time >= 31104000:
                return f'{round(year, 1)} years'
            elif 31104000 > obj_time >= 2592000:
                return f'{round(month, 0)} months'
            elif 2592000 > obj_time >= 86400:
                return f'{round(day, 0)} days'
            elif 86400 > obj_time >= 3600:
                return f'{hour} hours'
            elif 3600 > obj_time >= 60:
                return f'{min} minutes'
            else:
                return f'{obj_time} seconds'
        except AttributeError:
            return f'No data...'

    def __str__(self):
        return f'{self.timer_adjuster()}'


test = PasswordStrenghtTimer('nhfhdkf')
print(test)



