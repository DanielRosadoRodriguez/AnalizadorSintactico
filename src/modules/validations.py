def is_program_file(remaining_elements: list) -> list:
    if len(remaining_elements) >= 3:
        first_word = remaining_elements[0]
        program_name = remaining_elements[1]
        last_word = remaining_elements[-1]
        if first_word == 'PROGRAMA' and last_word == 'FINPROG' and program_name == '[id]':
            remaining_elements.pop(0)
            remaining_elements.pop(0)
            remaining_elements.pop()
            return is_sents_sent(remaining_elements[:])
    return remaining_elements


def is_sents_sent(remaining_elements: list) -> list:
    if len(remaining_elements) >= 2:
        result = remaining_elements[:]
        cont = 0
        while True:
            result = is_imprime_txt(result)
            result = is_imprime_elem(result)
            result = is_lee(result)
            result = is_assignment(result)
            cont += 1
            if cont == 5:
                return result
    return remaining_elements


def is_imprime_txt(remaining_elements: list) -> list:
    if remaining_elements:
        if len(remaining_elements) >= 2 and remaining_elements[0] == 'IMPRIME' and remaining_elements[1] == '[txt]':
            remaining_elements.pop(0)
            remaining_elements.pop(0)
            result = remaining_elements[:]
            return result
    return remaining_elements


def is_imprime_elem(remaining_elements: list) -> list:
    if remaining_elements:
        if len(remaining_elements) >= 2 and remaining_elements[0] == 'IMPRIME' and \
                remaining_elements[1] in ['[id]', '[valorn]']:
            remaining_elements.pop(0)
            remaining_elements.pop(0)
            return remaining_elements[:]
    return remaining_elements


def is_lee(remaining_elements: list) -> list:
    if remaining_elements:
        if remaining_elements[0] == 'LEE' and remaining_elements[1] in ['[id]', '[valorn]']:
            remaining_elements.pop(0)
            remaining_elements.pop(0)
            return remaining_elements[:]
    return remaining_elements


def is_assignment(remaining_elements: list) -> list:
    if remaining_elements:
        if len(remaining_elements) >= 3 and remaining_elements[0] == '[id]' and remaining_elements[1] == '=':
            assignment = remaining_elements[2:]
            result = is_operation(assignment)
            if assignment != result:
                return result
    return remaining_elements[:]


def is_elem(remaining_elements: list) -> list:
    if remaining_elements:
        if remaining_elements[0] in ['[id]', '[valorn]']:
            remaining_elements.pop(0)
            return remaining_elements
    return remaining_elements


def is_operation(remaining_elements: list) -> list:
    scope_elements: list = remaining_elements[:]
    if scope_elements:
        if len(scope_elements) > 2 and scope_elements[0] in ['[id]', '[valorn]'] \
                and scope_elements[1] in ['+', '-', '*', '/']:
            result: list = is_operation(scope_elements[2:])
            return result
        elif len(scope_elements) >= 2 and scope_elements[0] in ['[id]', '[valorn]'] \
                and scope_elements[1] not in ['+', '-', '*', '/']:
            scope_elements.pop(0)
            current_elements: list = scope_elements[:]
            return current_elements
        elif len(scope_elements) >= 1 and scope_elements[0] in ['[id]', '[valorn]']:
            scope_elements.pop(0)
            current_elements: list = scope_elements[:]
            return current_elements
        elif len(scope_elements) >= 2 and scope_elements[0] in ['[id]', '[valorn]'] and scope_elements[1] == '[id]':
            scope_elements.pop(0)
            current_elements = scope_elements[:]
            return current_elements
    return scope_elements
