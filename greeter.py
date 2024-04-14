from datetime import datetime

class Greeter:
    def greet(self, name):
        # Eliminar los espacios en blanco del nombre y capitalizar la primera letra
        name = name.strip().capitalize()
        # Devolver un mensaje de saludo con el nombre formateado
        return f"Hello {name}"


