from arbol import nodo


def buscar_solucion_BFS(estado_inicial, solucion):

    solucionado = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicial = nodo(estado_inicial)
    nodos_frontera.append(nodo_inicial)

    while (not solucionado) and len(nodos_frontera) != 0:

        nodos = nodos_frontera.pop(0)
        nodos_visitados.append(nodos)

        if nodo.get_datos() == solucion:

            solucionado = True
            return nodo

        else:

            dato_nodo = nodo.get_datos()

            hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
            hijo_izquierdo = nodo(hijo)

            if not hijo_izquierdo.en_lista(nodos_visitados) and not hijo_izquierdo.en_lista(nodos_frontera):

                nodos_frontera.append(hijo_izquierdo)

            hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
            hijo_central = nodo(hijo)

            if not hijo_central.en_lista(nodos_visitados) and not hijo_central.en_lista(nodos_frontera):

                nodos_frontera.append(hijo_central)

            hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
            hijo_derecho = nodo(hijo)

            if not hijo_derecho.en_lista(nodos_visitados) and not hijo_derecho.en_lista(nodos_frontera):

                nodos_frontera.append(hijo_derecho)

            nodo.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])