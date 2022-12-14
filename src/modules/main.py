from validations import *
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")
file_content = data_access.read_file("./../text_files/test.txt")
print(file_content)
txt = is_program_file(file_content)
print(txt)
print(is_operation(txt))