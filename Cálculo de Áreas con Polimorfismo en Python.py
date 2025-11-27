import math
''' 
 Importamos el módulo `math` para usar constantes y funciones matemáticas
 en este caso usamos `math.pi` para el valor de π y `math.pow()` para elevar potencias.

 -----------------------------
 Clase base (abstracta) Forma
 -----------------------------
''' 
class Forma:
    '''
     Esta clase actúa como una "interfaz" o clase abstracta.
     Define el método `calcularArea()` que debe implementar cualquier subclase.
     No implementamos la lógica aquí; en su lugar lanzamos una excepción para
     forzar a las subclases a proporcionar su propia implementación.
    '''
    def calcularArea(self):
        raise NotImplementedError("Subclase debe implementar calcularArea()")
    ''' 
         NotImplementedError es una forma de indicar que este método es abstracto:
         si alguien crea una clase que herede de Forma y no redefine calcularArea,
         llamar a calcularArea() provocará este error.
    '''
'''
 -----------------------------
 Clase Circulo (hereda de Forma)
 -----------------------------
'''
class Circulo(Forma):
    def __init__(self, radio):
        '''
         Guardamos el radio como atributo interno. Por convención usamos _radio
         para indicar que es de uso interno (encapsulamiento por convención).
        '''
        self._radio = radio

    def calcularArea(self):
        '''
         Fórmula del área del círculo: π * r^2
         math.pi es π y math.pow(self._radio, 2) eleva el radio al cuadrado.
         Devuelve un número (float).
        '''
        return math.pi * math.pow(self._radio, 2)
'''
 -----------------------------
 Clase Cuadrado (hereda de Forma)
 -----------------------------
'''
class Cuadrado(Forma):
    def __init__(self, lado):
        # Guardamos el lado del cuadrado
        self._lado = lado

    def calcularArea(self):
        # Área del cuadrado: lado^2
        return math.pow(self._lado, 2)
        # Alternativa equivalente: return self._lado ** 2
'''
 -----------------------------
 Clase Rectangulo (hereda de Forma)
 -----------------------------
'''
class Rectangulo(Forma):
    def __init__(self, base, altura):
        # Guardamos base y altura como atributos internos
        self._base = base
        self._altura = altura

    def calcularArea(self):
        # Área del rectángulo: base * altura
        return (self._base * self._altura)
'''
 -----------------------------
 Clase Triangulo (hereda de Forma)
 -----------------------------
'''
class Triangulo(Forma):
    def __init__(self, base, altura):
        # Guardamos base y altura del triángulo
        self._base = base
        self._altura = altura

    def calcularArea(self):
        # Área del triángulo: (base * altura) / 2
        return (self._base * self._altura) / 2
'''
 -----------------------------
 Creación de instancias (polimorfismo)
 -----------------------------
 Aquí creamos una lista con objetos de distintas subclases de Forma.
 Todas las clases heredan de Forma y por tanto tienen el método calcularArea.
'''
formas = [
    Circulo(5),        # círculo de radio 5
    Cuadrado(10),      # cuadrado de lado 10
    Rectangulo(7, 3),  # rectángulo de base 7 y altura 3
    Triangulo(4, 6)    # triángulo de base 4 y altura 6
]
'''
 -----------------------------
 Uso polimórfico de calcularArea()
 -----------------------------
'''
for forma in formas:
    '''
     No necesitamos saber el tipo concreto de `forma` aquí.
     Llamamos al mismo método `calcularArea()` y Python elegirá
     la implementación adecuada según la clase del objeto (dispatch dinámico).
    '''
    area = forma.calcularArea()
    '''
     Imprimimos el área. Aquí mostramos cómo cada subclase responde de forma distinta
     al mismo mensaje (calcularArea) — eso es polimorfismo.
    '''
    print(f"Area: {area}")
