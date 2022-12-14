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

