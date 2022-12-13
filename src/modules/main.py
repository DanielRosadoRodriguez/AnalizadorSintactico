import validations
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")

if validations.is_prog(file_content):
    print("its a program")
else:
    raise Exception('Its not a program')
