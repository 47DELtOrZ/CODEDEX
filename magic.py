import random

num = random.randint(1, 9)

1   ("yes definitely")
2   ("It is decidedly so")
3   ("Without a doubt")
4   ("Reply hazy, try again")
5   ("Ask again later")
6   ("Better not tell you now")
7   ("My sources say no")
8   ("Outlook not so good")
9   ("Very doubtful")

pregunta = int(input("¿cual es la pregunta?"))

#print(num)

if num == 1:
    print("yes definitely")

elif num == 2:
    print("It is decidedly so")

elif num == 3:
    print("Without a doubt")

elif num == 4:
    print("Reply hazy, try again")

elif num == 5:
    print("Ask again later")

elif num == 6:
    print("Better not tell you now")

elif num == 7:
    print("My sources say no")

elif num == 8:
    print("Outlook not so good")

elif num == 9:
    print("Very doubtful")

print(pregunta)
print(num)