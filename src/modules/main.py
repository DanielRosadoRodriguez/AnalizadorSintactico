from validations import *
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")
print(file_content)
print(is_program_file(file_content))
