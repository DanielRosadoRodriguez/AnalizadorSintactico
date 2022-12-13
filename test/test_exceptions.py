from src.modules.exeptions import CompilacionExitosaException


def test_compilacion_exitosa_exception():
    try:
        raise CompilacionExitosaException
    except CompilacionExitosaException:
        pass
