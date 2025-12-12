# Cálculo de Áreas con Polimorfismo 

Ejemplo educativo y limpio de **Programación Orientada a Objetos** que muestra cómo usar **herencia y polimorfismo** para calcular el área de diferentes figuras geométricas con el mismo método.

### Qué hace este código
- Define una clase base `Forma` que actúa como **interfaz** (método abstracto `calcularArea()`).
- Crea cuatro figuras que heredan de `Forma`:
  - `Circulo` → área = π × r²
  - `Cuadrado` → área = lado²
  - `Rectangulo` → área = base × altura
  - `Triangulo` → área = (base × altura) / 2
- Guarda todas las figuras en una lista (sin importar su tipo).
- Recorre la lista y llama al mismo método `.calcularArea()` en cada una → **polimorfismo en acción**.
