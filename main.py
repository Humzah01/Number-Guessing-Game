# Guess the number game code \/
import random

num1 = random.randint(1, 1000)
print('This is a game where you have to guess the number.')


guess = int(input("Guess the number "))

while num1 != guess:
	if(num1 < guess):
			guess = int(input("That is not the number. Guess a lower number. "))
			print()
	else:
			guess = int(input("That is not the number. Guess a higher number "))
			print()

print("That was correct! The number is " + str(num1))