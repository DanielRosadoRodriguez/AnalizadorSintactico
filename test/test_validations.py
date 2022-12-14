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


def test_is_operation():
    elements = ['[valorn]', '+', '[id]']
    assert len(validations.is_operation(elements)) == 0


def test_is_operation_2():
    elements = ['[valorn]', '+', '[id]', '-', '[valorn]', '/', '[id]', '*', '[valorn]']
    assert len(validations.is_operation(elements)) == 0


def test_is_not_operation_1():
    elements = ['[valorn]', '+', '[id]', '+']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_2():
    elements = ['[valorn]', '+', '-', '[id]', '+']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_3():
    elements = ['+', '[id]', '[id]']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_4():
    elements = ['[valorn]', '-', '+', '[id]', '-']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_5():
    elements = ['[valorn]', '*', '+', '[id]', '-']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_6():
    elements = ['[valorn]', '', '', '[id]', '*', '[id]', '[id]']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_7():
    elements = ['-', '[id]', '[id]']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_8():
    elements = ['/', '[id]', '[id]']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_9():
    elements = ['*', '[id]', '[id]']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_10():
    elements = ['[valorn]', '-', '[id]', '-']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_11():
    elements = ['[valorn]', '*', '[id]', '-']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_12():
    elements = ['[valorn]', '-', '[id]', '*']
    assert len(validations.is_operation(elements)) != 0


def test_is_not_operation_13():
    elements = ['[valorn]', '', '[id]', '']
    assert len(validations.is_operation(elements)) != 0


def test_is_imprime_txt():
    elements = ['IMPRIME', '[txt]']
    assert len(validations.is_imprime_txt(elements)) == 0


def test_is_not_imprime_txt():
    elements = ['[txt]', 'IMPRIME', '[txt]']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_txt_2():
    elements = ['[txt]']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_txt_3():
    elements = ['IMPRIME']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_txt_4():
    elements = ['IMPRIME', '[txt]', 'cualquiercosa']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_txt_5():
    elements = ['cualquiercosa']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_imprime_elem():
    elements = ['IMPRIME', '[id]']
    assert len(validations.is_imprime_elem(elements)) == 0


def test_is_imprime_elem_2():
    elements = ['IMPRIME', '[valorn]']
    assert len(validations.is_imprime_elem(elements)) == 0


def test_is_not_imprime_elem():
    elements = ['[txt]', 'IMPRIME', '[txt]']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_elem_2():
    elements = ['[txt]']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_elem_3():
    elements = ['IMPRIME']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_elem_4():
    elements = ['IMPRIME', '[txt]', 'cualquiercosa']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_not_imprime_elem_5():
    elements = ['cualquiercosa']
    assert len(validations.is_imprime_txt(elements)) != 0


def test_is_lee():
    elements = ['LEE', '[id]']
    assert len(validations.is_lee(elements)) == 0


def test_is_not_lee():
    elements = ['LEE', 'claquiercosa']
    assert validations.is_lee(elements) == ['LEE', 'claquiercosa']


def test_is_not_lee_2():
    elements = ['cualquiercosa', '[id]']
    assert validations.is_lee(elements) == ['cualquiercosa', '[id]']


def test_is_not_lee_3():
    elements = ['cualquiercosa']
    assert validations.is_lee(elements) == ['cualquiercosa']

