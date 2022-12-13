from src.modules import validations


def test_is_elem():
    elements: str = '[id]'
    assert validations.is_elem(elements)


def test_is_elem_2():
    elements: str = '[valorn]'
    assert validations.is_elem(elements)


def test_is_not_elem():
    elements: str = 'elementoRandom'
    assert validations.is_elem(elements) is False


def test_is_prog():
    first_word: str = 'PROGRAMA'
    last_word: str = 'FINPROG'
    assert validations.is_prog(first_word, last_word)


def test_is_not_prog_missing_programa():
    first_word: str = 'cualquiercosa'
    last_word: str = 'FINPROG'
    assert validations.is_prog(first_word, last_word) is False


def test_is_not_prog_missing_finprog():
    first_word: str = 'PROGRAMA'
    last_word: str = 'cualquiercosa'
    assert validations.is_prog(first_word, last_word) is False


def test_is_list_not_empty():
    elements: list = ['soy un elemento']
    assert validations.is_list_not_empty(elements)


def test_is_list_empty():
    elements: list = []
    assert validations.is_list_not_empty(elements) is False


def test_is_sent_imprime():
    first_word: str = 'IMPRIME'
    next_word: str = '[txt]'
    assert validations.is_sent_imprime(first_word, next_word)


def test_is_not_sent_imprime_first_word_not_imprime():
    first_word: str = 'cualquiercosa'
    next_word: str = '[txt]'
    assert validations.is_sent_imprime(first_word, next_word) is False


def test_is_not_sent_imprime_next_word_not_txt():
    first_word: str = 'IMPRIME'
    next_word: str = 'cualquiercosa'
    assert validations.is_sent_imprime(first_word, next_word) is False


def test_is_not_sent_imprime_both_incorrect_words():
    first_word: str = 'cualquiercosa'
    next_word: str = 'cualquiercosa'
    assert validations.is_sent_imprime(first_word, next_word) is False
