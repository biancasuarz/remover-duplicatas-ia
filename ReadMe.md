# Remoção de Duplicatas em Listas

Este script implementa uma função chamada `remover_duplicatas`, que remove duplicatas de uma lista mantendo a ordem original dos elementos.

## Função: `remover_duplicatas`

### Descrição
Recebe uma lista como entrada e retorna uma nova lista contendo apenas os elementos únicos, preservando a ordem de aparição.

### Parâmetros
- `array` (list): Lista de elementos de qualquer tipo.

### Retorno
- `list`: Lista com elementos únicos na mesma ordem de entrada.


## Informações para Instrutores
Qual foi a lógica usada?

- Criamos uma lista vazia chamada unicos, onde vamos armazenar os elementos únicos.
- Iteramos sobre cada item da lista original.
- A cada item, verificamos se ele já está presente na lista unicos.
- Se não estiver, adicionamos esse item à lista unicos.
- Se já estiver, pulamos para o próximo item.
- Retornamos a lista unicos, que contém apenas os primeiros elementos únicos, na mesma ordem em que apareceram.

### Como a IA nos ajudou (ou não) durante o processo?

- Sugeriu a estrutura inicial da função, o que agilizou o desenvolvimento.
- Ofereceu alternativas, como o uso de set para eliminar duplicatas, e uma solução com list comprehensions.
- Auxiliou na validação lógica com exemplos de casos de teste.

### O que alteramos das sugestões da IA e por quê?

Após discutirmos em equipe, decidimos não usar algumas das sugestões da IA:

- set: Embora eficiente, não preserva a ordem dos elementos, o que era um requisito.

- List comprehensions: Apesar de concisas, poderiam dificultar a compreensão do código por membros da equipe menos experientes.

Optamos por uma solução simples e legível, priorizando clareza e facilidade de manutenção. O trabalho em equipe e o uso da IA ajudaram a encontrar um equilíbrio entre eficiência e legibilidade.
