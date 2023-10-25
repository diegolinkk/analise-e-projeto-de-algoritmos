from .pilha import Pilha

def conversor_binario(decimal):
    p1 =  Pilha()
    while decimal > 0:
        p1.push(decimal % 2)
        decimal = decimal // 2
    
    while p1.is_empty() == False:
        print(p1.pop(), end=" ")

def conversor_de_base(numero,base):
    digitos = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if not(base>=2 and base <=36):
        return "erro"
    p1 = Pilha()
    while numero > 0:
        p1.push(digitos[numero % base])
        numero = numero // base
    
    while not p1.is_empty():
        print(p1.pop(), end=" ")