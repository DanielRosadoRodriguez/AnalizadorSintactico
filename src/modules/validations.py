def is_program_file(remaining_elements: list) -> list:
    if len(remaining_elements) >= 3:
        first_word = remaining_elements[0]
        program_name = remaining_elements[1]
        last_word = remaining_elements[-1]
        if first_word == 'PROGRAMA' and last_word == 'FINPROG' and program_name == '[id]':
            remaining_elements.pop(0)
            remaining_elements.pop(0)
            remaining_elements.pop()
            return remaining_elements
    return remaining_elements


def is_elem(remaining_elements: list) -> list:
    if remaining_elements:
        if remaining_elements[0] in ['[id]', '[valorn]']:
            remaining_elements.pop(0)
            return remaining_elements
    return remaining_elements


def is_operation(remaining_elements: list) -> list:
    if remaining_elements:
        revised_list = is_value(remaining_elements)
        if remaining_elements != revised_list:
            remaining_elements = revised_list
            if remaining_elements in is_operator(remaining_elements):
                is_operation(is_operator(remaining_elements))
                return remaining_elements
    return remaining_elements


def two_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

def is_value(remaining_elements: list) -> list:
    if remaining_elements:
        if remaining_elements[0] in ['[id]', '[valorn]']:
            remaining_elements.pop(0)
            return remaining_elements
    return remaining_elements


def is_operator(remaining_elements: list) -> list:
    if remaining_elements:
        if remaining_elements[0] in ['+', '-', '*', '/']:
            remaining_elements.pop(0)
            return remaining_elements
    return remaining_elements
