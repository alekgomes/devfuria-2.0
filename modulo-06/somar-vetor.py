
#
# processamento
#
def somarArray(array):
	soma = 0
	for n in array:
		soma = soma + n
	return soma

#
#saida
#

assert (60 == somarArray([10, 20, 30]))