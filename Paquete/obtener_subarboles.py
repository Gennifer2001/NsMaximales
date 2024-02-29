class obtener_subarbol:
    
    def asignar_nombres(arbol):

     for i, nodo in enumerate(arbol.traverse()):  #Asigna nombres a los nodos si no tienen uno
        if not nodo.name:
            nodo.name = f"Nodo_{i}"

    def obtener_subarboles(arbol):
        subarboles = []  #Inicializa una lista para almacenar los subárboles

        for nodo in arbol.traverse():  #Busca nodos descendientes del nodo iterado
            nodos_descendientes = arbol.search_nodes(name=nodo.name, order=1)

            subarbol = Tree()  #Construye un nuevo árbol con el nodo como raíz y sus descendientes
            subarbol.add_child(nodo.copy())

            for descendiente in nodos_descendientes:
                subarbol.add_child(descendiente.copy())

            subarboles.append(subarbol)

        return subarboles