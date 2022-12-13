from src.modules import data_access


def test_file_exist():
    path: str = "./text.txt"
    assert data_access.file_exists(path)


def test_file_does_not_exist():
    path: str = "im a nonexisting path"
    assert data_access.file_exists(path) is False


def test_read_file():
    path: str = "./text.txt"
    assert isinstance(data_access.read_file(path), list)


def test_file_content():
    path: str = "./text.txt"
    assert data_access.read_file(path) == [["texto", "de"], ["ejemplo"]]
