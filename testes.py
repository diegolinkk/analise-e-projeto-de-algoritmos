# from sorting.bubble_sort import bubble_sort
# from sorting.insertion_sort import insertion_sort
# from sorting.selection_sort import selection_sort
# from sorting.merge_sort import merge_sort
# from sorting.quick_sort import quick_sort
# from sorting.quick_sort_2 import quick_sort as quick_sort_2
# from random import sample
from sorting.reverse_sort import reverse_sort
from searching.verificar_item_duplicado import verificar_item_duplicado
from lists.pilha import Pilha
from lists.conversores_aritmeticos import conversor_binario, conversor_de_base
from lists.fila import Fila
from lists.deque import Deque

# lista_aleatoria = sample(range(1,1000),15)
# print(lista_aleatoria)

# lista1 = lista_aleatoria[:]
# print(f"Lista  antes do bubble_sort: {lista1}")
# bubble_sort(lista1)
# print(f"Lista  depois do bubble_sort: {lista1}\n")

# lista2 = lista_aleatoria[:]
# print(f"Lista  antes do insertion_sort: {lista2}")
# insertion_sort(lista2)
# print(f"Lista  depois do insertion_sort: {lista2} \n")


# lista3 = lista_aleatoria[:]
# print(f"Lista  antes do selection_sort: {lista3}")
# selection_sort(lista3)
# print(f"Lista  depois do selection_sort: {lista3} \n")

# lista4 = lista_aleatoria[:]
# print(f"Lista  antes do merge_sort: {lista4}")
# merge_sort(lista4)
# print(f"Lista  depois do merge_sort: {lista4} \n")


# lista5 = lista_aleatoria[:]
# print(f"Lista  antes do quick_sort: {lista5}")
# quick_sort(lista5)
# print(f"Lista  depois do quick_sort: {lista5} \n")


# lista6 = lista_aleatoria[:]
# lista6 = [5,3,2,1]
# print(f"Lista  antes do quick_sort 2: {lista6}")
# quick_sort_2(lista6)
# print(f"Lista  depois do quick_sort 2: {lista6} \n")

# TESTE DE INVERSÃO
lista = [3,3,3,3,3,4,5,1]
print(f"Lista ordenada {lista}")
reverse_sort(lista)
print(f"Lista invertida{lista}")

#TESTE DE VERIFICAR DUPLICADOS
lista = [1,2,3,4,5,6,7,8,9,10,4]
print(verificar_item_duplicado(lista))

# #TESTE PILHA
# p1 = Pilha()
# print(p1.is_empty())
# p1.push(1)
# p1.push(3)
# p1.push(5)
# print(p1.size())
# print(p1.is_empty())
# print(p1.peek())
# print(p1.peek())
# print(p1.peek())
# p1.clear()
# p1.push(12)
# print(p1.lista)
# print(p1.size())

#TESTE CONVERSOR BINÁRIO
# print("teste de conversores aritméticos:")
# conversor_binario(10)
# print("")
# conversor_binario(25)
# print("")

# conversor_de_base(16,16)
# print(" ")
# conversor_de_base(255,16)
# print(" ")
# conversor_de_base(332,16)
# print(" ")
# conversor_de_base(16,8)
# print(" ")
# conversor_de_base(25,2)
# print(" ")


## TESTES COM FILA
f1 = Fila()
f1.enqueue("Cachorro")
f1.enqueue("Gato")
f1.enqueue("Papagaio")
f1.enqueue("Cavalo")
f1.toString()
print(f1.size())
f1.dequeue()
f1.toString()
print(f1.size())
f1.dequeue()
f1.toString()
print(f1.size())
print(f1.peek())
f1.toString()
print(f1.size())
f1.dequeue()
f1.dequeue()
f1.dequeue()
f1.dequeue()
f1.dequeue()
f1.enqueue("Texugo")
f1.size()
f1.toString()
print(f1.size())


#testando deque
animais = Deque()
print("inicializando deque: ")
animais.to_string()
print("\n")
#adicionar tres itens
print("Adicionando três itens: ")
animais.add_back("cachorro")
animais.add_back("gato")
animais.add_back("papagaio")
animais.to_string()
print("\n")

#adicionar item no final
print("Adicionando item no final do deque")
animais.add_back("rinoceronte")
animais.to_string()

#adicionar item no começo
print("Adicionando itens no começo do deque")
animais.add_front("Ramster")
animais.to_string()

#remover item no final
print("Remover item do final do deque")
animais.remove_back()
animais.to_string()

#remover item no começo
print("Remover item no começo do deque")
animais.remove_front()
animais.to_string()

#remover item no final pela segunda vez
print("Remover item do final do deque pela segunda vez")
animais.remove_back()
animais.to_string()
#limpar lista

#remover item no começo pela segunda vez
print("Remover item no começo do deque  pela segunda vez")
animais.remove_front()
animais.to_string()

#remover ultimo elemento da lista
print("Remover ultimo elemento do deque")
animais.remove_back()
animais.remove_back()
animais.remove_front()
animais.to_string()

#adicionando mais um item na lista
print("Adicionando mais um item no deque")
animais.add_back("texugo")
animais.to_string()

#limpando a lista
print("limpando o deque")
animais.clear()
animais.to_string()