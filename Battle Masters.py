import random

#jan == 1 pd
#kien == 2 pa
#pou == 3 te


option = [1, 2, 3]

CPU = random.choice(option)

Move = int(input("Digite sua jogada: \n 1--Jan\n 2--Kien\n 3--Pou\n "))

if ((Move == 2 and CPU == 3) or (Move == 1 and CPU == 2) or (Move == 3 and CPU == 1)):
    print("Perdeu")
elif ((Move == 1 and CPU == 3) or (Move == 2 and CPU == 1) or (Move == 3 and CPU == 2)):
    print("Ganhou")
elif (Move == CPU):
    print("Empate")