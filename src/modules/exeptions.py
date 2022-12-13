class CompilacionExitosaException(Exception):
    def __init__(self, message='El programa ha terminado de compilarse'):
        self.message = message
        super().__init__(self.message)
