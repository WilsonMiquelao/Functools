from functools import reduce


lista_num = [1,2,3,4,5,6,7,8,9,10]

#fazendo a função para referenciar no funcao map

def calcular_quadrado(numero):
    return numero ** 2

#chamando a funcao map, para percorrer a lista_num,
#referenciando a funcao anteriormente criada e guardando na variavel potencia_list_num 

potencia_lista_num = list(map(calcular_quadrado, lista_num))

#printando o resultado

print(potencia_lista_num)

#funcao para identificar numeros pares e ser referenciada na funcao filter

def filtro_pares(numero):
    return numero % 2 == 0

#chamada da funcao filter, e referenciando a funcao filtro_pares anteriormente criada

num_pares = list(filter(filtro_pares, lista_num))

#printando o resultado

print(num_pares)

#utilizando a funcao reduce que pega o primeiro e o segundo numero, soma conforme a logica
#do lambda, e o resultado, soma com o proximo numero, "reduzindo" a lista a somente um elemento

soma = reduce(lambda x,y: x+ y, lista_num)

print(soma)


