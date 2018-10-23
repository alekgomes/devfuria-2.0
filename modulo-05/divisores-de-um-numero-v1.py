#-*- coding:utf-8 -*-

#
# entrada
#

#
# processamento
#
def encontraDivisores(n):
	divisores = []
	i = 1
	while i <= n:
		if n % i == 0:
			divisores.append(i)
		i += 1
	return divisores

#
#saída
#

assert([1, 2] == encontraDivisores(2))
assert([1, 2, 5, 10] == encontraDivisores(10))