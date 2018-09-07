#-*- coding: UTF-8 -*-

#
# entrada
#
x = eval(input('Entre com um lado da figura: '))
y = eval(input('entre com o outro lado da figura: '))

#
# processamento
#
def areaQuadrada(x, y):
	return x * y

#
# saida
#
assert (10 == areaQuadrada(2, 5))
print(f'A area da figura é {areaQuadrada(x,y)} u²')

