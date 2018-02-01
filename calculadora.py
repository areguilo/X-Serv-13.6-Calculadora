#/usr/bin/python3
import sys
num1 = float(sys.argv[2])
operation = sys.argv[1]
num2 = float(sys.argv[3])

if len(sys.argv)!=4:
    sys.exit("error de argumentos")
elif (operation == '+'):
    print (num1+num2)
elif (operation == "-"):
    print (num1-num2)
elif (operation == "x"):
    print (num1*num2)
else:
    try:
        print(num1/num2)
    except ZeroDivisionError:
        print("Zero Division Exception")
