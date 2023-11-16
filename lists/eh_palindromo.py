from .deque import Deque
def eh_palindromo(palavra):
    deque = Deque()
    for letra in palavra:
        deque.add_back(letra)
    
    valida_palindromo = True
    while(deque.count > 1 and valida_palindromo):
        comeco = deque.remove_front()
        fim = deque.remove_back()
        if fim != comeco:
            valida_palindromo = False
    
    if(valida_palindromo):
        print("A palavra {0} é um palíndromo".format(palavra))
    else:
        print("A palavra {0} não é um palíndromo".format(palavra))
