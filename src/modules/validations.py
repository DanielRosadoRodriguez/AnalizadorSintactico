
def is_prog(elements: list) -> bool:
    if elements[0] == 'PROGRAMA' and elements[-1] == 'FINPROG':
        return True
    else:
        return False


def is_elem(remaining_elements: list) -> bool:
    if remaining_elements[0] == "[id]" or remaining_elements[0] == "[valorn]":
        return True
    else:
        return False


def is_list_not_empty(elements: list) -> bool:
    if elements:
        return True
    else:
        return False
