#-*- coding: utf-8 -*-

#
# entrada
#

#
# processamento
#
def verifica(n):
    if n % 2 == 0:
        return True
    else:
        return False
#
# saída
#
assert (True == verifica(4))
assert (False == verifica(5))
