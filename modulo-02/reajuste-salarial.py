#-*- coding: utf-8 -*-

#
# entrada
#
salario = eval(input('Entre com o valor do salário a ser reajustado: '))
#
# processamento
#
def reajustarSalario(salario):
	return (salario * 0.15) + salario
#
# saída
#

assert (1150 == reajustarSalario(1000))
assert (2300 == reajustarSalario(2000))

print(f'Salário após reajuste: {reajustarSalario(salario)}')