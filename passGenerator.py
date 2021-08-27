#PASSSWORD GENERATOR !
#importuję biblioteki potrzebne do aplikacji
import random
import string

#Start - przywitanie użytkownika który wpisze na początek długośc hasła
print("Welcome to password generator:)")
passLen = int(input("Enter the lenght of password: "))

#Zmienne z których będzie składac się to hasło:
lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
num = string.digits
symbols = string.punctuation

#lączę te wszystkie zmienne
all = lowercase + uppercase + num + symbols

#losowanie z danych
temp = random.sample(all,passLen)

password = "".join(temp)

print(password)
