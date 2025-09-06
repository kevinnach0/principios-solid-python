
"""
Ejemplo del Principio de Responsabilidad Única (SRP).
Cada clase tiene una única responsabilidad:
- Estudiante: representar datos básicos de un estudiante.
- RegistroEstudiantes: encargarse de almacenar y mostrar registros.
"""

class Estudiante:
    """Representa los datos de un estudiante."""
    def __init__(self, nombre: str, edad: int, fecha_nacimiento: str):
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento

    def __str__(self):
        return f"{self.nombre}, {self.edad} años, nacido el {self.fecha_nacimiento}"


class RegistroEstudiantes:
    """Gestiona la lista de estudiantes registrados."""
    def __init__(self):
        self._estudiantes = []

    def agregar(self, estudiante: Estudiante):
        self._estudiantes.append(estudiante)

    def mostrar_registros(self):
        for est in self._estudiantes:
            print(est)


# ===============================
# DEMO
# ===============================
if __name__ == "__main__":
    print("--- SRP Demo ---")

    est1 = Estudiante("Kevin", 20, "04/01/2005")
    est2 = Estudiante("Ana", 22, "15/09/2003")

    registro = RegistroEstudiantes()
    registro.agregar(est1)
    registro.agregar(est2)

    registro.mostrar_registros()
