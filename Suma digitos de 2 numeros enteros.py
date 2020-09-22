#Escribe el código para leer dos números enteros(x, y)
# de dos dígitos y determina a cuánto es igual la suma de todos los dígitos. Imprime el resultado.

def reto4(x,y):
    
    x1=x//10
    x2=x%10
    
    y1=y//10
    y2=y%10
    

    resultado =x1+x2+y1+y2
    
    return resultado

reto4(3,4)
