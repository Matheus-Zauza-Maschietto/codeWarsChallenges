"""Criar uma tabela de multiplicação NxN do tamnho passado por parametro """

def multiplication_table(size):
    lista = [[x*y for y in range(1, size+1)] for x in range(1, size+1)]
    
    return lista

print(multiplication_table(3))
