class ListaUtils:

    def __init__(self):
        pass

    def particionar_lista(lista, n):
        inicio = 0
        for i in range(n):
            final = inicio + len(lista[i::n])
            yield lista[inicio:final]
            inicio = final

    def limpar_espacos_em_brancos(listao):
        return [int(item) for item in listao if item.isdigit()]