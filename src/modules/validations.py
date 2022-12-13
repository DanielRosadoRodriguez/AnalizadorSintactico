from src.modules.exeptions import CompilacionExitosaException


def is_prog(remaining_elements: list) -> bool:
    first_word: str = remaining_elements.pop(0)
    program_name: str = remaining_elements.pop(0)
    last_word: str = remaining_elements.pop()
    if first_word == 'PROGRAMA' and program_name == '[id]' and last_word == 'FINPROG':
        return True
    else:
        return False


def is_elem(remaining_elements: list) -> bool:
    word: str = remaining_elements.pop(0)
    if word == "[id]" or word == "[valorn]":
        return True
    else:
        return False


def is_sent_imprime(remaining_elements: list) -> bool:
    first_word: str = remaining_elements.pop(0)
    next_word: str = remaining_elements.pop(0)
    if first_word == 'IMPRIME' and next_word == '[txt]':
        return True
    else:
        return False


def is_list_not_emtpy(remaining_elements: list) -> bool:
    if remaining_elements:
        return True
    else:
        return False
