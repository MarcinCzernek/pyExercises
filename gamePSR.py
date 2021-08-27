import random

aiChoose = random.randint(1,3)

if(aiChoose == 1):
    aiChoose = str('Scissors')
elif(aiChoose == 2):
    aiChoose = str("Rock")
elif(aiChoose == 3):
    aiChoose = str("Paper")

youChoose = input("Type what you choose: 'Rock','Paper','Scissors' : ")

if(aiChoose == "Rock" and youChoose == "Paper"):
  print("You win")
elif(aiChoose == "Paper" and youChoose == "Rock"):
  print("You loose")

if(aiChoose == "Rock" and youChoose == "Scissors" ):
    print("You win!")
elif(aiChoose == "Scissors" and youChoose == "Rock"):
    print("You loose")

if(aiChoose == "Scissors" and youChoose == "Paper"):
    print("You loose")
elif(aiChoose == "Paper" and youChoose == "Scissors"):
    print("You win")

if(aiChoose == "Scissors" and youChoose == "Scissors"):
    print("Remis!")
elif(aiChoose == "Rock" and youChoose == "Rock"):
    print("Remis!")
elif(aiChoose == "Paper" and youChoose == "Paper"):
    print("Remis!")

print("--------------------")
print("You choose " + youChoose)
print("Oponent choose " + aiChoose)