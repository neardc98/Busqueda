from arbol import nodo

def buscar_bfs(estado_inicial, solucion):
    solucionando = False
    nodos_visitados = []
    nodos_fronteras = []
    nodo_inicial = nodo(estado_inicial)
    nodos_fronteras.append[nodo_inicial]

    while not solucionando and len(nodos_fronteras) != 0:
        nodos = nodos_fronteras.pop(0)
        nodos_visitados.append(nodos)

        if nodo.get_datos() == solucion:
            solucionando = True
            return nodo
        else:
            datos = nodo.get_datos()

            hijo = [datos[0], datos[1], datos[2], datos[3]]
            hijo_izquierdo = nodo(hijo)

            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_fronteras):
                nodos_fronteras.append(hijo_izquierdo)

            hijo = [datos[0], datos[2], datos[1], datos[3]]
            hijo_central = nodo(hijo)

            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_fronteras):
                nodos_fronteras.append(hijo_central)

            hijo = [datos[0], datos[1], datos[3], datos[2]]
            hijos_derecha = nodo(hijo)

            if not hijos_derecha.en_lista(nodos_visitados) and not hijos_derecha.en_lista(nodos_fronteras):
                nodos_fronteras.append(hijos_derecha)

            nodo.set_hijos([hijo_izquierdo,hijo_central,hijos_derecha])