# clase persona

class Persona:

    #metodo constructor
    def __init__(self,nombre,apellidos,edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad


    # metodo para mosrrar los datos de una persona
    def MostrarPersona(self):
        print("nombre: " + self.Nombre)
        print("apellidos:" + self.Apellidos)
        print("edad: "+ str(self.Edad))

# metodo principal
def main():
    p1 = Persona("miguelin","galvis", 15)
    p1.MostrarPersona()
    p2 = Persona("carlitos","montañita",17)
    p2.MostrarPersona()
    p1.Edad = 14
    p1.MostrarPersona()
    p1 =p2
    p1.MostrarPersona
    p2.MostrarPersona

if __name__ == "__main__":
    main()

