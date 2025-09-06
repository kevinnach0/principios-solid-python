
# Ejemplo de proyecto para portafolio: SOLID (L, I, D) aplicado
from abc import ABC, abstractmethod
from typing import  List


# -----------------------------
# MÓDULO: liskov_module
# Ejemplo: Figuras geométricas que cumplen con LSP.
# -----------------------------


class Shape(ABC):
    @abstractmethod 
    def area(self) -> float:
        pass


class Rectangle(Shape):
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height


    def area(self) -> float:
        return self.width * self.height


class Square(Shape):
    def __init__(self, side: float):
        self.side = side


    def area(self) -> float:
        return self.side * self.side

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius


    def area(self) -> float:
        return 3.14159 * self.radius * self.radius

def total_area(shapes: List[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

def demo_liskov():
    """Función pública que demuestra Liskov (puede importarse desde main).
    """
    print("--- Liskov demo ---")
    shapes = [Rectangle(2, 3), Square(4), Circle(2)]
    print("Áreas:", [s.area() for s in shapes])
    print("Área total:", total_area(shapes))
