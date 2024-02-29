class obtener_maximal:
    def es_contenido(subarbol1, subarbol2):
      """
      Verifica si subarbol1 está contenido en subarbol2.
      """
      raiz_subarbol1 = subarbol1.children[0]   #Obtiene el nodo raíz del subarbol1, accediendo al primer hijo del subárbol

      for nodo_subarbol2 in subarbol2.traverse():  #Itera sobre los nodos del subarbol2
          if nodo_subarbol2.name == raiz_subarbol1.name:  #Verifica si el nombre del nodo raíz de subarbol1 está en subarbol2
              return True
              break
      return False


    def obtener_maximales(n_subarboles):
        """
        Obtiene los n-subarboles maximales a partir de la lista de n-subarboles.
        """
        maximales = []  #Inicializa una lista para los maximales en cada n
        subarboles_no_maximales = set()

        for n, subarboles in n_subarboles:
            subarboles_maximales = []  #Inicializa una lista para los maximales

            if n == 1:  #Los 1-subárboles siempre son maximales
                subarboles_maximales.extend(subarboles)
                maximales.append((n, subarboles_maximales))
            else:
                for subarbol in subarboles:
                    if len(subarbol.get_leaf_names()) == n:  #Los n-subárboles con exactamente n hojas siempre son maximales
                        subarboles_maximales.append(subarbol)
                    else:
                        es_maximal = True
                        for otro_subarbol in subarboles:  #Comprueba si el subárbol está contenido en otro subárbol
                            if subarbol != otro_subarbol and es_contenido(subarbol, otro_subarbol):
                                es_maximal = False
                                subarboles_no_maximales.add(subarbol)  #Agrega el subárbol no maximal al conjunto para no volver a revisarlo después
                                break

                        if es_maximal and subarbol not in subarboles_no_maximales:  #Verifica si es maximal y no se ha marcado como no maximal antes
                            subarboles_maximales.append(subarbol)

                maximales.append((n, subarboles_maximales))

        return maximales 
