
gryffindor=0
ravenclaw=0
hufflepuff=0
slytherin=0

p1 = int(input())
r1 = int(input("introduce tu respuesta 1-2"))

print("p1)Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")

if r1 ==1:
    gryffindor += 1
    ravenclaw += 1 

elif r1 ==2:
    hufflepuff += 1
    slytherin +=1

else: 
  print("wrong input")


p2 = int(input())
r2 = int(input("introduce tu respuesta 1-4"))
print("p2)When I’m dead, I want people to remember me as")
print("1) The good")
print("2) The great")
print("3) The wise")
print("4) The bold")

if r2 == 1:
  hufflepuff += 1
elif r2 == 2:
  slytherin +=1
elif r2 == 3:
  ravenclaw +=1
elif r2 == 4:
  gryffindor +=1

else:
  print("wrong input")

p3 = int(input())
r3 = int(input("introduce tu respuesta 1-4"))
print("p3)Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

if r3 == 1:
  slytherin +=1
elif r3 == 2:
  hufflepuff +=1
elif r3 == 3:
  ravenclaw +=1
elif r3 == 4:
  gryffindor +=1

else:
  print("wrong input")

