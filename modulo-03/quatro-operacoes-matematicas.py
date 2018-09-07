#-*- coding:utf-8 -*-

#
# entrada
#
print('#'*4, 'MENU', '#'*4)
print('1 - Somar\n2 - Multiplicar\n3 - Subtrair\n4 - Dividir')
escolha = int(input('Escolha: '))


num1 = eval(input('Entre com primeiro numero: '))
num2 = eval(input('Entre com segundo numero: '))

#
# processamento
#
if escolha == 1:
	def somar(num1, num2):		
		return num1 + num2

	assert(20  == somar(10, 10))
	print(f'A soma é igual a {somar(num1, num2)}')

elif escolha == 2:
	def multiplicar(num1, num2):
		return num1 * num2

	assert(100 == multiplicar(10, 10))
	print(f'A multiplicação é igual a {multiplicar(num1, num2)}')

elif escolha == 3:
	def subtrair(num1, num2):
		return num1 - num2

	assert(10  == subtrair(20, 10))
	print(f'A subtração é igual a {subtrair(num1, num2)}')

elif escolha == 4:
	def dividir(num1, num2):
		return num1 / num2
		
	assert(4 == dividir(12, 3))
	print(f'A divisão é igual a {dividir(num1, num2)}')

