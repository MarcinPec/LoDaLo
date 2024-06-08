import pytest
import string
import l2e_genpass_engine
import l1e_assoc_bigram_genpass_engine
import l3e_genlogin_engine

"""
Tests for l2e_genpass_engine module
"""

@pytest.fixture
def password_generator():
    return l2e_genpass_engine.GenPass


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_all_true(password_generator, length):
    test = password_generator(length, True, True, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_numbsletters_true(password_generator, length):
    test = password_generator(length, True, True, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_numbs_true(password_generator, length):
    test = password_generator(length, True, False, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isdigit() for char in str(test))


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_letters_true(password_generator, length):
    test = password_generator(length, False, True, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_special_true(password_generator, length):
    test = password_generator(length, False, False, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_lettersspecial_true(password_generator, length):
    test = password_generator(length, False, True, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize("length", [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25])
def test_password_numbsspecial_true(password_generator, length):
    test = password_generator(length, True, False, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


"""
Tests for l1e_assoc_bigram_genpass_engine module
"""

@pytest.fixture
def assoc_password_generator():
    return l1e_assoc_bigram_genpass_engine.AsociationalBigramPassGen


@pytest.mark.parametrize('word1', ["samochód", "dom", "jabłko", "kot", "pies", "telefon", "książka",
    "komputer", "kwiat", "drzewo", "słońce", "butelka", "krzesło",
    "kawa", "piłka", "telewizor", "łóżko", "biurko", "szkoła", "ryba"])
@pytest.mark.parametrize('word2', ["apple", "banana", "car", "house", "dog", "cat", "book",
    "computer", "flower", "sun", "phone", "chair", "coffee",
    "ball", "table", "school", "tree", "fish", "bird", "desk"])
def test_assoc_password_all_true(assoc_password_generator, word1, word2):
    test = assoc_password_generator(word1, word2, True, True, True)
    for _ in range(10):
        assert any(char.isalpha() for char in str(test)) # Czy zawiera litery
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize('word1', ["samochód", "dom", "jabłko", "kot", "pies", "telefon", "książka",
    "komputer", "kwiat", "drzewo", "słońce", "butelka", "krzesło",
    "kawa", "piłka", "telewizor", "łóżko", "biurko", "szkoła", "ryba"])
@pytest.mark.parametrize('word2', ["apple", "banana", "car", "house", "dog", "cat", "book",
    "computer", "flower", "sun", "phone", "chair", "coffee",
    "ball", "table", "school", "tree", "fish", "bird", "desk"])
def test_assoc_password_polish_true(assoc_password_generator, word1, word2):
    test = assoc_password_generator(word1, word2, True, True, False)
    for _ in range(10):
        assert any(char.isalpha() for char in str(test)) # Czy zawiera litery
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize('word1', ["samochód", "dom", "jabłko", "kot", "pies", "telefon", "książka",
    "komputer", "kwiat", "drzewo", "słońce", "butelka", "krzesło",
    "kawa", "piłka", "telewizor", "łóżko", "biurko", "szkoła", "ryba"])
@pytest.mark.parametrize('word2', ["apple", "banana", "car", "house", "dog", "cat", "book",
    "computer", "flower", "sun", "phone", "chair", "coffee",
    "ball", "table", "school", "tree", "fish", "bird", "desk"])
def test_assoc_password_english_true(assoc_password_generator, word1, word2):
    test = assoc_password_generator(word1, word2, True, False, True)
    for _ in range(10):
        assert any(char.isalpha() for char in str(test)) # Czy zawiera litery
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


"""
Tests for l3e_genlogin_engine module
"""


@pytest.fixture
def login_generator():
    return l3e_genlogin_engine.GenLog


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_all_true(login_generator, pattern, length):
    test = login_generator(pattern, length, True, True, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_numbers_letters_true(login_generator, pattern, length):
    test = login_generator(pattern, length, True, True, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_numbers_special_true(login_generator, pattern, length):
    test = login_generator(pattern, length, True, False, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjaln


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_letters_special_true(login_generator, pattern, length):
    test = login_generator(pattern, length, False, True, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_numbers_true(login_generator, pattern, length):
    test = login_generator(pattern, length, True, False, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isdigit() for char in str(test))  # Czy zawiera co najmniej jedną cyfrę


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_letters_true(login_generator, pattern, length):
    test = login_generator(pattern, length, False, True, False)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char.isalpha() for char in str(test))  # Czy zawiera co najmniej jedną literę


@pytest.mark.parametrize('pattern', ['olusia', 'bruce', 'tyrant'])
@pytest.mark.parametrize('length', [8, 9, 10, 11, 12, 25, 35, 45])
def test_login_special_true(login_generator, pattern, length):
    test = login_generator(pattern, length, False, False, True)
    for _ in range(1000):
        assert len(str(test)) == length
        assert any(char in string.punctuation for char in str(test))  # Czy zawiera co najmniej jeden znak specjalny

