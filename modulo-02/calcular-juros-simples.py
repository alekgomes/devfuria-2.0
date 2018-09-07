#-*- coding:UTF-8 -*-

#
# entrada
#
capital = eval(input('Capital a ser considerado: '))
taxa_de_juros = eval(input('Taxa de juros (forma decimal): '))
periodo_em_meses = eval(input('Período de empréstimo (em meses): '))
#
# processamento
#
def calcularJuros(capital, taxa_de_juros, periodo_em_meses):
	return capital * taxa_de_juros * periodo_em_meses
#
# saída
#

assert (20   == calcularJuros(100, 0.1, 2))
assert (2560 == calcularJuros(16000, 0.04, 4))

print(f'O juros a ser pago nessas condições é de {calcularJuros(capital, taxa_de_juros, periodo_em_meses)}')