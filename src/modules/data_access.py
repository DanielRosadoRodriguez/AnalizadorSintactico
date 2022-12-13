import os


def file_exists(path: str):
    if os.path.isfile(path):
        return True
    else:
        return False


def read_file(path: str):
    if file_exists(path):
        return get_file_content(path)
    else:
        raise Exception("File does not exist")


def get_file_content(path):
    content = []
    with open(path, 'r') as file:
        for line in file:
            content.extend(line.rstrip().split())
    return content
