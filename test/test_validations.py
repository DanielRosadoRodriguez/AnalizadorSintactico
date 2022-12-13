from src.modules import validations


def test_is_elem():
    elements: list = ['[id]', 'elementoRandom']
    assert validations.is_elem(elements)


def test_is_elem_2():
    elements: list = ['[valorn]', 'elementoRandom']
    assert validations.is_elem(elements)


def test_is_not_elem():
    elements: list = ['[elementoKKS', 'elementoRandom']
    assert validations.is_elem(elements) is False


def test_is_prog():
    elements: list = ['PROGRAMA', 'cualquiercosa', 'elementoDePrueba', 'FINPROG']
    assert validations.is_prog(elements)


def test_is_not_prog_missing_finprog():
    elements: list = ['PROGRAMA', 'cualquiercosa', 'elementoDePrueba']
    assert validations.is_prog(elements) is False


def test_is_list_not_empty():
    elements: list = ['soy un elemento']
    assert validations.is_list_not_empty(elements)


def test_is_list_empty():
    elements: list = []
    assert validations.is_list_not_empty(elements) is False
