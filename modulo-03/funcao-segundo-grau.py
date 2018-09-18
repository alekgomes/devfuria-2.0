# Escrever código que calcule as raízes de uma
# equação de segundo grau
from math import sqrt
#
# entrada
#

#
# processamento
#

def encontra_delta(a, b, c):
	delta = (b * b) - (4 * a * c)
	return delta

def encontra_x1(a, b, c):
	delta = encontra_delta(a, b, c)
	x1 = (-b + sqrt(delta)) / 2
	return x1

def encontra_x2(a, b, c):
	delta = encontra_delta(a, b, c)
	x2 = (-b -sqrt(delta)) / 2
	return x2

#
# saída
#

assert (64 == encontra_delta(1, 0, -16))
assert ( 4 == encontra_x1(1, 0, -16))
assert (-4 == encontra_x2(1, 0, -16))