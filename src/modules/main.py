import validations
import data_access

file_content = data_access.read_file("./../text_files/prueba.lex")
if len(validations.is_program_file(file_content)) == 0:
    print("Compilación Exitosa")
else:
    print("Se han encontrado errores")
