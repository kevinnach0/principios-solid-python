
from typing import Protocol
# -----------------------------
# MÓDULO: isp_module
# Ejemplo: Documentos con capacidades separadas (imprimir, guardar).
# -----------------------------


class Printable(Protocol):
    def print_content(self) -> str: ...




class Savable(Protocol):
    def save(self, filename: str) -> None: ...




class Report(Printable, Savable):
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content


    def print_content(self) -> str:
        return f"Reporte: {self.title}\n{self.content}"


    def save(self, filename: str) -> None:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(self.print_content())




class Note(Printable):  
    def __init__(self, text: str):
        self.text = text


    def print_content(self) -> str:
        return f"Nota: {self.text}"
    

def demo_isp():
    """Función pública que demuestra Interface Segregation.
    """
    print("--- ISP demo ---")
    report = Report("Ventas", "Total: 1000")
    note = Note("Revisar inventario")
    print(report.print_content())
    print(note.print_content())
    report.save("reporte.txt")
    print("Reporte guardado en 'reporte.txt'")
