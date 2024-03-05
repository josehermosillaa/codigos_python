Algoritmo numero_primos
	Escribir "ingrese un numero"
	Leer n
	cont<-0
	
	Para i<-1 Hasta n Hacer
		si n%i=0 Entonces
			cont<- cont + 1
		FinSi
		si cont >2 
		FinSi
	FinPara
	
	si cont = 2 Entonces
		Escribir n," Es un numero primo"
	SiNo
		Escribir n," No es un numero primo"
	FinSi
	
FinAlgoritmo
