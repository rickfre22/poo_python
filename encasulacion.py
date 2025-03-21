



# clase coordenada

class Coordenada:
    
    # Metodo constructor
    def __init__(self,x,y):
        #atributos privados
        self.__X = x
        self.Y = y

    #metodo de lectura y escritura de cada atributo
    def getx(self):
        return self.__X
    
    def getx(self):
        return self.__Y
    
    def setX(self, x):
        self.__X= x

    def setX(self, y):
        self.__Y= y

    #metodo para mosttrar coordenada
    def mostrarCoordenada(self):
        print("(",self.__X,",",self.__Y, ")")

# clase cuadrado

class Cuadrado:

    # metodo constructor
    def __init__(self, v1, v2, v3, v4):
        # atributos privados
        self.__V1 = v1
        self.__V2 = v2
        self.__V3 = v3
        self.__V4 = v4

        # metodos privados para mostrar los vertices
        def _mostrarCoordenadav1(self):
            print("(",self.__V1.getX(),"," ,self.__V1.getY(),")")

        def _mostrarCoordenadav1(self):
            print("(",self.__V2.getX(),"," ,self.__V2.getY(),")")

        def _mostrarCoordenadav1(self):
            print("(",self.__V3.getX(),"," ,self.__V3.getY(),")")

        def _mostrarCoordenadav1(self):
            print("(",self.__V4.getX(),"," ,self.__V4.getY(),")")

        # metodo para mostrar los vertices
        def mostrarVertices(self):
            print("el cuadrado esta compuesto por los siguientes vertices: ")
            self.__mostrearCoordenadaV1()
            self.__mostrearCoordenadaV2()
            self.__mostrearCoordenadaV3()
            self.__mostrearCoordenadaV4()


#metodo principal de modulo
def main():
    #input
    x1 = int(input("dijite el valor de x: "))
    x2 = int(input("dijite el valor de y: "))

    #proccesiing
    c1 = Coordenada(x1,x2)
    c1.mostrarCoordenada()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)
    v4 = Coordenada(10,5)

    Cuadrado1 = Cuadrado(v1,v2,v3,v4)
    Cuadrado1.mostrarVertices()

    # que ocurre si el metodo getX() lo hacemos privado:__getX()?
    coordenada = Coordenada(3,4)
    print("(",coordenada.getX(),",", coordenada.getY(),")")

if __name__=="__main__":
    main()