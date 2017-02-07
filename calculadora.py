import sys

if len(sys.argv)!= 4:
	sys.exit("error de entrada")
_, oper, oper1, oper2 = sys.argv

oper1 = float(oper1)
oper2 = float(oper2)

if oper == 'suma':
	hacer = oper1 + oper2
elif oper == 'mult':
	hacer = oper1 * oper2
elif oper == 'resta':
	hacer = oper1 - oper2
elif oper == 'div':
	try:
     		hacer = oper1 / oper2
	except ZeroDivisionError:
 		print ("No se permite la división por cero")
if oper2 != 0:
	print (hacer)
