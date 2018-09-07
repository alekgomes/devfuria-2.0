#
# entrada
#
numero = int(input('Entre com um número inteiro: '))
#
# processamento
#
def antecessor(n):
	return n - 1

def sucessor(n):
	return n + 1 

#
# saída
#

assert (10 == sucessor(9))
assert (8  == antecessor(9))

print(f'O sucessor de {numero} é {sucessor(numero)}')
print(f'O antecessor de {numero} é {antecessor(numero)}')