
# entrada
numero = int(input('Entre com um numero: '))

# processamento
def calculaDobro(numero):
	return 2 * numero

# saida
assert (20 == calculaDobro(10))
assert (100 == calculaDobro(50))

print(f'O dobro de {numero} é {calculaDobro(numero)}')