def is_prog(first_word: str, last_word: str) -> bool:
    if first_word == 'PROGRAMA' and last_word == 'FINPROG':
        return True
    else:
        return False


def is_elem(word: str) -> bool:
    if word == "[id]" or word == "[valorn]":
        return True
    else:
        return False


def is_list_not_empty(elements: list) -> bool:
    if elements:
        return True
    else:
        return False


def is_sent_imprime(first_word: str, next_word: str) -> bool:
    if first_word == 'IMPRIME' and next_word == '[txt]':
        return True
    else:
        return False

