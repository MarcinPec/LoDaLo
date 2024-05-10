from string import ascii_letters


def gen_express_str(func):
    def wrapper(*args, **kwargs):
        function = func(*args, **kwargs)
        result = ''.join(function)
        return result
    return wrapper


def gen_express_list(func):
    def wrapper(*args, **kwargs):
        function = func(*args, **kwargs)
        result = list(function)
        return result
    return wrapper


class EncryptTXT:
    def __init__(self, data2encrypt):
        self.data2encrypt = data2encrypt

    def encryption(self):
        with open(self.data2encrypt, 'r') as data:
            ready_data = data.read()
            norm = ascii_letters
            rever = ascii_letters[::-1]
            translation_table = str.maketrans(norm, rever)
            encrypted_text = ready_data.translate(translation_table)[::-1]
        with open(self.data2encrypt, 'w') as data:
            data.write(encrypted_text)
        return encrypted_text

    def __str__(self):
        return f'{self.encryption()}'
