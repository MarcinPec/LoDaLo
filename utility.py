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
