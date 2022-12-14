from validations import *
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")
file_content = data_access.read_file("./../text_files/test.txt")
file_content = data_access.read_file("./../text_files/test2.txt")
print(file_content)
print(is_assignment(file_content))
