import random

def user_guess(x):
	random_number = random.randint(1, x)
	guess = 0
	lives = 6


	while guess != random_number and lives > 0:
		guess = int(input(f"Guess the number between 1 and {x}: "))
		lives -= 1
		if lives < 0:
			print("No more lives left. Game over!") 
		elif guess < random_number:
			print("Wrong! Random number is higher. Try again")
			print(f"You have {lives} left!")
		elif guess > random_number:
			print("Wrong! Random number is lower. Try again")
			print(f"You have {lives} left!")
		elif guess == random_number:
			print("Congrats! You win!")
		

def computer_guess(x):
	hi = x
	low = 1
	feedback = ""
	guess = 0
	lives = 6
	
	while feedback != "c" and lives >= 0:
		lives -= 1
		guess = random.randint(low, hi)
		feedback = input(f"Is {guess} to High (H), to Low (L) or Correct (C)?").lower()

		if lives < 0: 
			 print("Computer has no lives left. User wins! Congrats!")
		elif feedback == "h":
			hi = guess - 1
			print(f"Computer lives left: {lives}")
		elif feedback == "l":
			low = guess + 1
			print(f"Computer lives left: {lives}")
		elif feedback == "c":
			print("Computer wins!")	
			pass


game_mode = input("Hello! Please choose your Game mode:\
Guess number (G) or Vs PC (P): ").lower()
x = int(input("Enter the range of the game from 1 to:"))

if game_mode == "g":
	user_guess(x)
else:
	computer_guess(x)
