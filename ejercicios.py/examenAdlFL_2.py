#Realiza un programa que pida el dí­a de la semana (del 1 al 7) y escriba el día correspondiente. Si introducimos otro número nos da un error y nos vuelve a solicitar el número de día.(Aitor de la Fuente Lopez 23-02-2023)

num=(int(input("Dame un numero entre el 1 y el 7")))

if num ==1:
    print("Lunes")

elif num ==2:
    print("Martes")

elif num ==3:
    print("Miercoles")

elif num ==4:
    print("Jueves")

elif num ==5:
    print("Viernes")

elif num ==6:
    print("Sabado")

elif num ==7:
    print("Domingo")

