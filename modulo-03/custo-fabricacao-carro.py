#-*- coding: utf-8 -*-

#
# processamento
#

def calcula_preco(custo):
	porcentagem_distribuidor = 0.28;
	porcentagem_imposto      = 0.45; 
	return custo + (custo * porcentagem_distribuidor) + (custo * porcentagem_imposto)
#
#saida
#
assert (17300 == calcula_preco(10000))
