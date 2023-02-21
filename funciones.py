"""
Funtion module
"""

def sumar(x,y):
    return x+y
    
def es_primo(numero):
    return numero > 1 and all(numero % i != 0 for i in range(2, int(numero ** 0.5) + 1))
   
