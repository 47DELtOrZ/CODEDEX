cla=int(input("dame una clave"))
con=int(input("dame una contraseña"))

while cla != ("dame una clave"):
    cla=int(input("No se prosigue hasta que la clave sea 0987"))

if con != ("dame una contraseña"):
    con=int(input("No se prosigue hasta que el codigo sea admin"))

print(cla,con)

