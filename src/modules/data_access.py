import os


def file_exists(path: str):
    if os.path.isfile(path):
        return True
    else:
        return False


def read_file(path: str):
    content: list = []
    with open(path, 'r') as file:
        for line in file:
            content.append(line.rstrip().split())
        return content
