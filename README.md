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
    
