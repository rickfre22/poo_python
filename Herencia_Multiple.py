# Definimos la primera clase padre
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        return f"{self.nombre} está comiendo."  # Usamos f-string

# Definimos la segunda clase padre
class Volador:
    def volar(self):
        return f"{self.nombre} está volando a gran altura."  # Usamos f-string

# Creamos una clase que hereda de ambas clases
class Halcon(Animal, Volador):
    def __init__(self, nombre):
        super().__init__(nombre)

# Instanciamos un objeto de la clase Halcon
halcon = Halcon("Fénix")

# Accedemos a los métodos de ambas clases padre
print(halcon.comer())  # Método de la clase Animal
print(halcon.volar())  # Método de la clase Volador  

    

