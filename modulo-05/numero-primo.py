
#
# processamento
#

def ehPrimo(n):
	contador = 0
	i = 1
	while i <= n:
		if n % i == 0:
			contador += 1
		i += 1 
	if contador > 2:
		return False
	else: 
		return True
#
# saida
#
assert(True == ehPrimo(5))
assert(False == ehPrimo(6))