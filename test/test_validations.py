from src.modules import validations


def test_is_elem():
    elements: list = ['[id]', 'cualquiercosa']
    assert validations.is_elem(elements)


def test_is_elem_2():
    elements: list = ['[valorn]']
    assert validations.is_elem(elements)


def test_is_not_elem():
    elements: list = ['elementoRandom']
    assert validations.is_elem(elements) is False


def test_is_prog():
    elements: list = ['PROGRAMA', '[id]', 'FINPROG']
    assert validations.is_prog(elements)


def test_is_not_prog_missing_programa():
    elements: list = ['cualquiercosa', '[id]', 'FINPROG']
    assert validations.is_prog(elements) is False


def test_is_sent_imprime():
    elements = ['IMPRIME', '[txt]']
    assert validations.is_sent_imprime(elements)


def test_is_not_sent_imprime_first_word_not_imprime():
    elements = ['cualquiercosa', '[txt]']
    assert validations.is_sent_imprime(elements) is False


def test_is_not_sent_imprime_next_word_not_txt():
    elements = ['IMPRIME', 'cualquiercosa']
    assert validations.is_sent_imprime(elements) is False


def test_is_not_sent_imprime_both_incorrect_words():
    elements = ['cualquiercosa', 'cualquiercosa']
    assert validations.is_sent_imprime(elements) is False


def test_is_an_empty_list():
    elements = []
    assert validations.is_list_not_emtpy(elements) is False
