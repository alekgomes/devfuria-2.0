#-*- coding: utf-8 -*-

#
# entrada
#
meses = eval(input('Entre com a quantidade de meses: '))

#
# lógica
#
def mesesEmDias(meses):
	return meses * 30
#
# saída
#
assert(60  == mesesEmDias(2))
assert(120 == mesesEmDias(4))

print(f'{meses} meses somam um total de {mesesEmDias(meses)} dias')