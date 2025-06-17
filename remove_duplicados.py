def remove_duplicados(arr):
    return list(set(arr))

lista = [1, 2, 2, 3, 4, 4, 5,'a', 'b', 'a', '', 'c', 'b', '', 'd']
resultado = remove_duplicados(lista)
print(resultado)

def remove_duplicados_ordem(arr):
    unicos = []
    for item in arr:
        if item not in unicos:
            unicos.append(item)
    return unicos

resultado_ordem = remove_duplicados_ordem(lista)
print(resultado_ordem)  
