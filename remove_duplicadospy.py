def remove_duplicados(arr):
    return list(set(arr))

# Teste da função remove_duplicados
lista = [1, 2, 2, 3, 4, 4, 5,'a', 'b', 'a']
resultado = remove_duplicados(lista)
print(resultado)  # Saída: [1, 2, 3, 4, 5] (a ordem pode variar devido ao uso de set)

def remove_duplicados_ordem(arr):
    unicos = []
    for item in arr:
        if item not in unicos:
            unicos.append(item)
    return unicos

# Teste da função remove_duplicados_ordem
resultado_ordem = remove_duplicados_ordem(lista)
print(resultado_ordem)  # Saída: [1, 2, 3, 4, 5]
