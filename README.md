# poo en py

introduccion a la POO  en python
- el paradigma de POO esta basado en una abstraccion del mundo real  que nos va a permitir desarrollar programas de forma mas cercana a com venos el mundo, pensado en objetos que tenemos delante y en acciones que podemos hacer con ellos.

## clase 
- una clase es un tipo de dato cuyas variables se llaman objetos o instsancias.
- la clase es la definicion del copcepto del mundo real y los objetos o instqancias son el propio objeto del mundo real.
- las clases estan compuestas por dos elementos:atriburos y metodos

### atributos
- informacion que almacena la clase

### metodos
- operaciones  que pueden realizar las clases

## definicon de una clase en py

```python
class nombreclase:

    def__init__(self,variabe1,variable):
        self.atributo1 =valor 1
        self.atributo2 = valor 2

    def nombremetodo(self):
        bloquecodigo
```
### componetes

```class```: para reservada en py para definir una clase.

```nombreclase```:nombre de la clase que quieres crear.

```def```: palabra reservada enpythonque se utiliza para definir tanto el cnstructor de la clase (metodo que se ejecuta primera vez que usas una clase)como los doiferentes metodos que tiene.

```__init__````: palabra reservada en pytho para defenir el metodo constructor de la clase. es lo primero que se ejecuta cuando crear un objeto de una clase.

```(self, variablex)```:parametro del construcor de la clase. el parametro self es obligatorio despues puedes tener tantos pametros como quieras la forma de añadir parametro es la misma que en las  funciones.

```self.atributox```:forma de utilizacion y acceos de los atributos de la clase.

```nombre metodo```:nombre del metodo de la clase

```(self)```:parametros del metodo. el parametro self es obligatorio y despues puedes tener tantos parametros como quierasla forma de añadir parametro es la misma que en las  funciones.

```bloquecodigo```:n¡instrucciones que ejecuara el metodo.

- cuando define una clase debes tener e cuenta los siguentes puntos:
    
- puedes definir atributos como necesites como tambien metodos, paraamtros en el constructor y  en los metodos como necesites
    

## composicion
- consiste en la creacion de nuevas clases a partir de otras clases ya rxistente que actuan como elementos compositores de la nuevas
_ las clases existentes sera atributos de la nueva clase.
- el POO la composicion significa que entre las dos clases existe una relacion de tipo 1
- ejemplo:
    - una cordenada en 2 dimenciones esta compuesta por dos valores ,el valor en el eje de las x y el valor de las y, esto podria ser una clase. un cuadrado esta compuesto  por 4 coordenadas que son los 4 vertices,esto podria ser una claseque esta compuesta por 4 clases del objeto coordenada 
## Encapsulación
- Se trata de la protección de los datos de usos o accesos no controlados.
- Los datos (atributos) que componen una clase pueden ser de dos tipos:
    - Públicos:  los datos son accesibles sin control, es decir, los datos pueden ser usados sin ningún tipo de mecanismo que proteja ante usos no autorizados o indebidos.
    - Privados: los datos no pueden ser accedidos sin control y para acceder a ellos se deberá implementar un método que acceda a ellos.  De esta forma, los datos serán accedidos única y directamente por la propia clase.
- La encapsulación no solo puede realizarse sobre los atributos de la clase, también es posible realizarla sobre los métodos, es decir, aquellos métodos que indiquemos que son privados no podrán ser utilizados por elementos externos al propio objeto.
- La definición de atributos y metodos privados se realiza incluyendo los caracteres "__" (dos guiones de piso) entre la palabra "self" y el nombre del atributo.

## Herencia
- Permite la reutilización de código.
- Consiste en la definición de una clase utilizando como base una clase ya existente.
- La nueva clase derivada tendrá todas las caracteristicas de la clase base y ampliará el concepto de esta, es decir, tendrá todos los atributos y métodos de la clase base.
- Significa que entre dos clases existe una relación del tipo "es un".
- La herencia en Python se especifica de la siguiente manera: ```class NombreClase(ClaseBase):```
- Ejemplo:
    - Pensemos en una persona como una clase, la persona tendría una serie de atributos como pueden ser el nombre, los apellidos, la edad, etc.  Esas características de una persona serían compartidas por todas aquellas clases hijas como pueden ser alumno y profesor.  Es decir, alumno y profesor heredarían las propiedades de la clase persona y tendrían sus propias propiedades, diferentes entre ellas, como por ejemplo el curso en el que está el alumno y el horario de tutorias del profesor.

    - Clase base: Persona
        - Atributos:
            - Nombre
            - Apellidos
            - Edad

    - Clase derivada: Alumno
        - Atributos:
            - Curso
            - Asignaturas
    
    - Clase derivada: Profesor
        - Atributos:
            - Antigüedad
            - Tutorias
            - Teléfono

## Actividad:
- Consulte un ejemplo práctico del uso de herencia múltiple en Python

### Bibliografía
Moreno, A. y Córcoles, S.  (2020).  Python práctica.  Herramientas, conceptos y técnicas.  Ediciones de la U.