n = int(input("Digite um numero: "))
fibA = 1
fibB = 0

if n == 1 or n == 0:
	print(True)
	exit

else:
	while n > fibA:
		aux = fibA
		fibA = fibA + fibB 
		fibB = aux

	print(n == fibA)
	