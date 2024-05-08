
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

n_subs = obtener_n_subarboles(todos_subarboles, 20)

def obtener_texto(subarbol):
    return subarbol.write(format=9)

for n, subarboles in n_subs:
    print(f"Subárboles con tamaño {n}:")
    for subarbol in subarboles:
        print(obtener_texto(subarbol))
    print("\n")

maximales = obtener_maximales(n_subs)

Sn = calcular_sn(maximales)

Base_resultados = base_topologica(Sn, maximales)

# Filtrar por rango de edad de 12-18 años
edades1 = df[df['age']=='12-18']
A = list(edades1.index.astype(str))

adherencia(Base_resultados, A, df)
```

La salida de `adherencia` será una lista de índices que pertenecen al conjunto y un DataFrame con estos puntos filtrados.

## Resultados

### Subárboles Máximos

Subárboles máximos con diferentes tamaños:

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

### Otros Resultados

- Valor máximo en Sn: (4, 9072)
- El valor de n es 4
- Base topológica B_4: [['0', '19', '11'], ['14', '13', '12'], ['2', '1'], ['9', '4', '18', '3'], ['8', '7'], ['15', '17', '10'], ['16', '6', '5']]

## Uso Adicional

Para hallar los puntos topológicos, filtra la base de datos según se desee. Por ejemplo, filtramos los datos por el rango de edad de 12-18 años:

```python
# Filtrar por rango de edad de 12-18 años
edades1 = df[df['age']=='12-18']
A = list(edades1.index.astype(str))

adherencia(Base_resultados, A, df)
```

Esto devolverá una lista de adherencia con los índices correspondientes.

![Python](READ_ME/python.pdf)
```

Puedes copiar este contenido y pegarlo directamente en tu archivo `README.md`. Asegúrate de ajustar las rutas de las imágenes (`dendro.pdf` y `python.pdf`) según la estructura de tu proyecto. Además, asegúrate de que la sintaxis Markdown sea correcta para que el contenido se muestre correctamente en GitHub.
