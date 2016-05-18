res = "s"
while res=="s":
	print "suma(1),resta(2),multiplicacion(3),division(4),potencia(5)"

        print "modulo(6), Exponencial(7), Raiz Cuadrada(8), Seno(9), Coseno(0))"
        opc = input("Ingrese la Opcion deseada: ")
	if opc == 1:
		
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		suma = num1 + num2
		print suma
	elif opc == 2:
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		resta = num1 - num2
		print resta
	elif opc == 3:
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		multi = num1 * num2
		print multi
	elif opc == 4:
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		divi = num1 / num2
		print divi
	elif opc == 5:
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		poten = num1**num2
		print poten
	elif opc == 6:
		num1 = input("ingrese primer numero: ")
		num2 = input("ingrese segundo numero: ")
		modul = num1%num2
		print modul
	elif opc == 7:
                import math
		num1 = input("ingrese el numero: ")
		expo = math.exp(num1)
		print (expo)
        elif opc == 8:
                import math
		num1 = input("ingrese el numero: ")
		raiz = math.sqrt(num1)
		print (raiz)  
        elif opc == 9:
                import math
		num = input("ingrese el numero: ")
		sen1 = math.sin(num)
		print (sen1)
        elif opc == 0:
                import math
		num = input("ingrese el numero: ")
		cos = math.cos(num)
		print (cos) 
	else:
		print ("Ingrese la opcion del 1-8")
	res = raw_input("Desea seguir?(s/n): ")

print "Vuelva pronto"
