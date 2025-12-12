# Area Calculation with Polymorphism

Educational and clean example of **Object-Oriented Programming** that demonstrates how to use **inheritance and polymorphism** to calculate the area of different geometric shapes using the same method.

### What this code does

* Defines a base class `Shape` that acts as an **interface** (abstract method `calculateArea()`).
* Creates four shapes that inherit from `Shape`:

  * `Circle` → area = π × r²
  * `Square` → area = side²
  * `Rectangle` → area = base × height
  * `Triangle` → area = (base × height) / 2
* Stores all shapes in a list (regardless of type).
* Iterates through the list and calls the same `.calculateArea()` method on each → **polymorphism in action**.
