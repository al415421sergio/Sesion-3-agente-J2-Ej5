Ik=float(input('Escribe el interes nominal: '))
m=float(input('Escribe cada cuantos meses es capitalizable: '))

k=m/12
Mk=1+Ik/(100*k)
TAE=100*(Mk**k-1)
TAE=round(TAE, 2)

print('El TAE es: '+ str(TAE))
