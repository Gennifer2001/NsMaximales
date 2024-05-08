Empecemos con la instalación del paquete con el siguiente codigo

```python
!pip install git+https://github.com/Gennifer2001/NsMaximales.git
```
y para cargar cada una de las funciones se necesita

```python
from Paquete.convertir_a_arbol import convertir_a_Tree
from Paquete.obtener_subarboles import asignar_nombres,obtener_subarboles
from Paquete.obtener_n_subarboles import obtener_n_subarboles
from Paquete.obtener_maximales import obtener_maximales
from Paquete.calcular_sn import calcular_sn
from Paquete.base_topologica import base_topologica
from Paquete.Puntos_topologicos import Exterior,Interior,Limite,Frontera,Adherencia
from Paquete.operadores_topologicos import exterior,interior,limite,frontera,adherencia
```
Para ilustrar el uso del código, presentaremos un breve ejemplo usando un dendrograma de 20 hojas.

![Dendrograma arbitrario con 20 hojas](READ_ME/dendro.pdf)

```python
arbol = convertir_a_Tree(dendo, leaf_names=range(0,20))
print(arbol.write(format=9))
```

```
(((((13,12),14),(2,1)),((((18,3),4),9),(8,7))),((((17,10),15),((6,5),16)),((19,11),0)));
```

Para obtener subárboles y visualizarlos:

```python
asignar_nombres(arbol)
todos_subarboles = obtener_subarboles(arbol)
#Ambas funciones requieren como parámetro el árbol obtenido en la función anterior

n_subs = obtener_n_subarboles(todos_subarboles,20)
#En este caso se requieren los subárboles obtenidos anteriormente y el número de datos. Para poder visualizarlos se puede definir la siguiente función

def obtener_texto(subarbol):
    return subarbol.write(format=9) #Usándolo de la siguiente manera
for n, subarboles in n_subs:
    print(f"Subárboles con tamaño {n}:") #El texto de este print se puede cambiar
    for subarbol in subarboles:
        print(obtene_texto(subarbol))
    print("\n")
#Teniendo los n−subárboles vemos los maximales

maximales = obtener_maximales(n_subs)
#Usando como parámetro la asignación de las listas de n−subárboles. Visualizandolo de la misma forma
```
.
.
.

- Tamaño 17:
  ```
  (((((13,12),14),(2,1)),((((18,3),4),9),(8,7))));
  ((((17,10),15),((6,5),16)),((19,11),0));
  ```

- Tamaño 18:
  ```
  (((((13,12),14),(2,1)),((((18,3),4),9),(8,7))));
  ((((17,10),15),((6,5),16)),((19,11),0));
  ```

- Tamaño 19:
  ```
  (((((13,12),14),(2,1)),((((18,3),4),9),(8,7))));
  ((((17,10),15),((6,5),16)),((19,11),0));
  ```

- Tamaño 20:
  ```
  ((((((13,12),14),(2,1)),((((18,3),4),9),(8,7))),((((17,10),15),((6,5),16)),((19,11),0))));
  ```


```python
Sn = calcular_sn(maximales)
#Se usa la asignación de los n−subárbols maximales

Base_resultados = base_topologica(Sn, maximales)
#Los parámetros son la lista de Sn y los n−subárboles maximales. La salida es
```

- Valor máximo en Sn: (4, 9072)
- El valor de n es 4
- Base topológica B_4: [['0', '19', '11'], ['14', '13', '12'], ['2', '1'], ['9', '4', '18', '3'], ['8', '7'], ['15', '17', '10'], ['16', '6', '5']]

```python
#Para hallar los puntos topológicos filtramos la base de datos según se quiera. En este caso filtramos los datos por el rango de edad de 12-18 años
edades1 = df[df[’age’]==’12-18’]

#Se crea una lista con los índices de la base de datos
A = list(edades1.index.astype(str))

#Los parámetro para todos los puntos son las asignaciones de la base, la lista de índices y la base de datos usada respectivamente. La salida de cada uno es una lista con los índices que pertenecen al conjunto y un dataframe con estos puntos filtrados. Por ejemplo:
Adherencia(Base_resultados,A,df
```
```
Adherencia = [’9’, ’4’, ’18’, ’3’]
```
![Python](READ_ME/python.pdf)

Si se necesita unicamente el resultado de los operadores topologicos sin una base de datos se debe utilizar el nombre del conjunto sin mayuscula y devuleve unicamenete la lista

```python
adherencia(Base_resultados,A)
```
```
Adherencia = [’9’, ’4’, ’18’, ’3’]
```

Las funciones de 'operadores_topologicos' se utilizan para calcular los operadores topológicos de una base o incluso de una topología, almacenando este conjunto como una lista de objetos en Python que pueden ser asignados a la variable 'Base_topologica'. Esto permite que el código se utilice no solo para análisis topológico de datos, sino también para cálculos más simples.
