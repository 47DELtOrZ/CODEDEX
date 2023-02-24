#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día. (Haz dos versiones: una sin utilizar listas y otra con listas)(Aitor de la Fuente Lopez 23-02-2023).

num=(int(input("Dame un numero entre el 1 y el 7")))
dds=["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

while  num<1 or num>7:
   print("Error")
   num=(int(input("dame otro")))

   print(dds[num-1])


for i in range (0,7):
   print(dds)


   


   



