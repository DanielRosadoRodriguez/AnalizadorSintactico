from validations import *
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")
if is_program_file(file_content) == []:
    print("compilación exitosa")
else:
    print("error al compilar")
