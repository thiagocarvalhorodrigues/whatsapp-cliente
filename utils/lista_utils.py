class ListaUtils:

    def __init__(self):
        pass

    def particionar_lista(lista, n):
        inicio = 0
        for i in range(n):
            final = inicio + len(lista[i::n])
            yield lista[inicio:final]
            inicio = final










#
# class ListaUtils:
#
#     def __init__(self):
#         pass
#
#     def particionar_lista(lista, n):
#         inicio = 0
#         for i in range(n):
#             final = inicio + len(lista[i::n])
#             yield lista[inicio:final]
#             inicio = final
#             print("Final  =", final)
#             print("Inicio  =",inicio)