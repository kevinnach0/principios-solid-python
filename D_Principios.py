
from typing import Protocol

#Realizar 3 ejericcios de el ultimo principio# -----------------------------
# MÓDULO: dip_module
# Ejemplo: Generador de reportes que depende de una abstracción Exporter.
# -----------------------------



class Exporter(Protocol):
    def export(self, data: str) -> None: ...




class ConsoleExporter:
    def export(self, data: str) -> None:
        print("[Consola]", data)




class FileExporter:
    def __init__(self, filename: str):
        self.filename = filename


    def export(self, data: str) -> None:
        with open(self.filename, "w", encoding="utf-8") as f:
            f.write(data)


class ReportManager:
    def __init__(self, exporter: Exporter):
        self.exporter = exporter


    def generate_report(self, text: str) -> None:
        self.exporter.export(f"*** Reporte ***\n{text}")
def demo_dip():
    """Función pública que demuestra Dependency Inversion.
    """
    print("--- DIP demo ---")
    console_exporter = ConsoleExporter()
    file_exporter = FileExporter("salida.txt")
    manager_console = ReportManager(console_exporter)
    manager_file = ReportManager(file_exporter)
    manager_console.generate_report("Datos en consola")
    manager_file.generate_report("Datos en archivo")
    print("Reporte guardado en 'salida.txt'")
