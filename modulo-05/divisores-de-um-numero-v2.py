#-*- coding:utf-8 -*-

#
# entrada
#

#
# processamento
#
def encontraDivisores(n):
	divisores = []
	for i in range(1, n+1):
		if n % i == 0:
			divisores.append(i)
	return divisores

#
#saída
#

assert([1, 2] == encontraDivisores(2))
assert([1, 2, 5, 10] == encontraDivisores(10))