import matplotlib.pyplot as plt

def calcular_sn(maximales):
    """
    Calcula y devuelve la lista Sn a partir de la lista de n-subárboles maximales y grafica los resultados.
    """
    Sn = []  # Inicializa la lista para los valores de Sn

    for n, subarboles in maximales:
        Sj = len(subarboles)  # Inicializa con la cantidad de n-subárboles maximales
        for subarbol in subarboles:
            Sj *= len(subarbol)  # Actualiza Sj con el valor de la operación
        Sn.append((n, Sj))

    # Limitar la lista de tuplas a las primeras 25
    lista_tuplas = Sn[:25]

    # Extraer las coordenadas x e y de las tuplas
    x_coords = range(1, len(lista_tuplas) + 1)  # Valores consecutivos de 1 en 1
    y_coords = [tupla[1] for tupla in lista_tuplas]
    # Graficar los puntos y conectarlos con líneas
    plt.plot(x_coords, y_coords, marker='o', linestyle='-')
    # Establecer los valores de las etiquetas del eje x
    plt.xticks(x_coords)
    # Etiquetas de los ejes
    plt.xlabel('Valor de n')
    plt.ylabel('Valor de Sn')
    # Título del gráfico
    plt.title('Variación de Sn')
    # Mostrar el gráfico
    plt.grid(True)
    plt.show()

    return Sn

