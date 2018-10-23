#-*- coding: utf-8 -*-

#
# entrada
#

#
# processamento
#
def isPositive(n):
	if n >= 0:
		return True
	else:
		return False

#
# saída
#
assert (True == isPositive(3))
assert (False == isPositive(-3))