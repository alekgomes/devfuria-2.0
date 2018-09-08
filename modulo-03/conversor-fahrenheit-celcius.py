#-*- coding: utf-8 -*-

#
# entrada
#
print('#'*3, 'Conversor', '#'*3)
print('1 - DE fahrenheit PARA celsius ')
print('2 - DE celsius PARA fahrenheit ')
escolha = eval(input('Sua escolha: '))

#
# processamento
#

def toCelsius(fahrenheit):
	return (fahrenheit - 32) / 9 * 5

def toFahrenheit(celsius):
	return celsius * 9 / 5 + 32


if escolha == 1:	
	fahrenheit = eval(input('Temperatura em Fahrenheit: '))
	
	print(f'{fahrenheit} Fahrenheit equivale a {toCelsius(fahrenheit)} Celsius')

elif escolha == 2:
	celsius = eval(input('Temperatura em Celsius: '))

	print(f'{celsius} Celsius equivale a {toFahrenheit(celsius)} Fahrenheit')

else:
	print('Escolha inválida')

assert 100  == toCelsius(212)	
assert 212 == toFahrenheit(100)
