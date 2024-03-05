Algoritmo numeros_pares
	N = 1	
	resultado = 0
	Mientras  N <=100
		
		si N mod 2 = 0  Escribir N
			resultado = resultado + N
		FinSi
		N = N + 1
	FinMientras
	Escribir "la suma total de numeros pares es " resultado
FinAlgoritmo