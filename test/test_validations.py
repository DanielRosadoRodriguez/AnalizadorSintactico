from src.modules import validations


def test_is_program_file():
    elements = ['PROGRAMA', '[id]', 'FINPROG']
    assert len(validations.is_program_file(elements)) == 0


def test_is_not_program_file_1():
    elements = ['PROGRAMA', 'cualquiercosa', 'FINPROG']
    assert len(validations.is_program_file(elements)) != 0


def test_is_not_program_file_2():
    elements = ['PROGRAMA', 'cualquiercosa', 'FINPROG']
    assert len(validations.is_program_file(elements)) != 0


def test_is_not_program_file_3():
    elements = ['cualquiercosa', '[id]', 'FINPROG']
    assert len(validations.is_program_file(elements)) != 0


def test_is_not_program_file_4():
    elements = ['PROGRAMA', '[id]', 'cualquiercosa']
    assert len(validations.is_program_file(elements)) != 0


def test_is_not_program_file_5():
    elements = ['PROGRAMA']
    assert len(validations.is_program_file(elements)) != 0


def test_is_elem():
    elements = ['[id]']
    assert len(validations.is_elem(elements)) == 0


def test_is_elem_2():
    elements = ['[valorn]']
    assert len(validations.is_elem(elements)) == 0


def test_is_not_elem():
    elements = ['cualquiercosa']
    assert len(validations.is_elem(elements)) != 0


def test_is_value():
    elements = ['[valorn]']
    assert len(validations.is_value(elements)) == 0


def test_is_value_2():
    elements = ['[id]']
    assert len(validations.is_value(elements)) == 0


def test_is_not_value():
    elements = ['cualquiercosa']
    assert len(validations.is_value(elements)) != 0


def test_is_operator():
    elements = ['+']
    assert len(validations.is_operator(elements)) == 0


def test_is_operator_2():
    elements = ['-']
    assert len(validations.is_operator(elements)) == 0


def test_is_operator_3():
    elements = ['*']
    assert len(validations.is_operator(elements)) == 0


def test_is_operator_4():
    elements = ['/']
    assert len(validations.is_operator(elements)) == 0


def test_is_not_operator():
    elements = ['cualquiercosa']
    assert len(validations.is_operator(elements)) != 0


def test_is_operation():
    elements = ['[valorn]', '+', '[id]']
    assert len(validations.is_operation(elements)) == 0
