# Uso
En este proyecto realizamos las diferentes operaciones matematicas de forma modular. Tambien tenemos un archivo principal de nombre ```a11g2.py``` en el cual importamos las funciones desde sus respectivos archivos y realizamos algunos calculos, asimismo tiene algunas funciones nativas del mismo archivo las cuales se encargan de calcular diferentes cosas.

## Funcionamiento
Recomiendo utilizar el programa desde la terminal, importando sus funciones directamente.
Para ello, primero debemos movernos al directorio donde tenemos nuestro archivo y entonces ejecutar el siguiente comando:
```bash
python or python3
```
y luego importamos todas las funciones con:
```python
from a11g2.py import *
```
Ahora ya tenemos todas las funciones importadas, sientase libre de explorar las mismas.
** En los titulos del tutorial se especifica como se debería llamar a cada una de las funciones **

### ing2i
Esta funcion permite el ingreso de dos numeros, y los retorna, se puede utilizar para asignar esos dos numeros a dos variables.
```python
>>> x,y=ing2i()
ingrese el primer numero: 1
ingrese el segundo numero: 2
>>> x
1
>>> y
2
```
### ing2s
Esta funcion permite el ingreso de dos datos tipo string, y los retorna, se puede utilizar para asignar esos dos valores a dos variables.
```python
>>> x,y = ing2s()
ingrese el primer string: hola
ingrese el segundo string: agu
>>> x
'hola'
>>> y
'agu'
```
### p1(parametro1, paremetro2, paremetro3)
Esta funcion devuelve el producto del primer parametro por el segundo, y le suma el tercero.
```python
>>> p1(1,2,3)
5
```
### p2(a, b, c)
Esta función devuelve la suma del primer parametro por el segundo y al resultado lo multiplica por el tercero.
```python
>>> p2(1,2,3)
9
```
### p3(x, y, c)
Esta función devuelve la resta del primer parametro por el segundo y lo multiplica por el tercero.
```python
>>> p3(1,2,3)
-3
```
### genrnd()
Esta función genera y devuelve una lista de numeros pseudo-aleatorios comprendidos entre el -256 y el 256.
```python
>>> lista = genrnd()
>>> lista
[17, -116, -119, 230, -34, -102, 214, -64, -225, 209, -235, -136, 129, 163, -46, -215, -190, -236, -238, 167, -188, -136, -215, -23, -142, -120, 186, -202, 17, -209, 183, -17, -211, 122, 41, -83, -59, 239, -214, 229, -254, -187, -133, -190, 253, -136, 187, -119, 84, -28]
```
### suma_lista(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve la suma de todos los elementos comprendidos dentro de la misma.
```python
>>> suma_lista(lista)
-2152
```
### producto_lista(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve una lista de la misma longitud que la original con el producto de varios elementos de la lista elegidos de forma aleatoria.
```python
>>> producto_lista(lista)
[25840, 22950, 42750, 35156, 44935, 29240, -23146, 5236, 40018, 3910, 40018, 26554, -11928, -11424, 41239, 5474, 2312, 50932, 39083, 35530, 34882, -19007, -9614, 22950, 43430, 17762, 32637, -2023, 44506, -29104, -43554, 29541, -19740, -31787, 43737, 29104, 2193, 45220, 28063, 4063, 15776, -11638, 7080, 22372, 49742, 43430, -782, -39345, -13570, 12138]
```
### cociente_lista(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve una lista de la misma longitud que la original con el cociente de varios elementos de la lista elegidos de forma aleatoria.
```python
>>> cociente_lista(lista)
[-2.5180722891566263, -1.0222222222222221, 0.7272727272727273, -0.9172932330827067, 1.8907563025210083, -1.0262008733624455, -0.5375494071146245, 10.764705882352942, 1.0053475935828877, 0.3925233644859813, -6.195121951219512, -1.4166666666666667, -1.054263565891473, 0.6325581395348837, 1.351063829787234, 4.086956521739131, 0.7260869565217392, 1.6379310344827587, 1.0, -2.7976190476190474, 0.8947368421052632, -0.9207920792079208, 3.0602409638554215, 1.2780748663101604, -0.6200873362445415, -0.14166666666666666, 1.1176470588235294, -1.2279411764705883, 0.08133971291866028, 0.4338235294117647, 0.84251968503937, 0.5395348837209303, -0.6397849462365591, -1.2822085889570551, 1.3970588235294117, 0.19327731092436976, 5.5, 0.25, 0.698744769874477, 6.323529411764706, -0.6397849462365591, -0.9090909090909091, 0.8823529411764706, -3.152542372881356, 1.0163934426229508, 0.2857142857142857, -0.7957446808510639, 0.0794392523364486, -5.5, 2.5217391304347827]
```
### calcula_media(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve la media de la misma.
```python
>>> calcula_media(lista)
-43.04
```
### calcula_mediana(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve la mediana de la misma.
```python
>>> calcula_mediana(lista)
-1076.0
```
### calcula_rango(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve el rango de la misma.
```python
>>> calcula_rango(lista)
[-254, 253]
```
### calcula_varianza(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve la varianza de la misma.
```python
>>> calcula_varianza(lista)
160.836
```
### calcula_min(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve el numero mas bajo de la misma.
```python
>>> calcula_min(lista)
-254
```
### calcula_max(lista)
A esta función se le debe pasar una lista por parametro, nos devuelve el numero mas alto de la misma.
```python
>>> calcula_max(lista)
253
```
### genrnd5e()
Esta función devuelve una lista con 5.000.000 de numeros pseudo-aleatorios comprendidos entre -256 y 256.
```python
>>> lista2 = genrnd5e()
```
No se imprime la misma dentro del readme por razones obvias.
### tiempo_ejecucion()
Esta función tiene dos partes, la primera calcula el tiempo en correr todas las funciones desde calcula_mediana hasta calcula_max primero con una lista simple de 50 elementos y luego calcula el tiempo de ejecución de las mismas funciones pero utilizando la lista de 5.000.000 elementos.
Se utiliza con el fin de evidenciar la congestión que genera el tener que realizar tantos calculos asi mismo sean realizados por la computadora.
```python
>>> tiempo_ejecucion()
Primer bloque: 0:00:00.000375 
Segundo bloque: 0:00:05.888198 
Diferencia: 0:00:05.887823
```





