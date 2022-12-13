import validations
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")

first_element = file_content.pop(0)
last_element = file_content.pop()

if validations.is_prog(first_element, last_element):
    print("its a program")
else:
    raise Exception('Its not a program')
