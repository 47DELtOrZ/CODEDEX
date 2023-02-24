#Pide al usuario un número del 1 al 12 y escribe el número del mes correspondiente (1 = enero, 2= febrero,..) usando un array

num=(int(input("dame un numero entre 1 y 12")))

meses=[("enero"),("febrero"),("marzo"),("abril"),("mayo"),("junio"),("julio"),("agosto"),("septiembre"),("octubre"),("noviembre"),("diciembre")]

while  num<1 or num>12:
   print("Fallo")
   num=(int(input("dame otro")))
   
   print(meses[num-1])