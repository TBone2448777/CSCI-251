#I forgot what this is called, but here it goes
solved = 0
import random
# word_bank = ["summer", "chalk", "painstaking", "float", "spotless", "canvas", "launch", "whimsical", "cook", "accessible", "porter", "descriptive", "concern", "bump", "jeans", "pretend", "aberrant", "rural", "cap", "empty", "misty", "glorious", "fish", "imaginary", "present", "remind", "suggestion", "complain", "development", "powder", "axiomatic", "calculate", "mom", "ultra", "nippy", "frequent", "thoughtless", "cagey", "wretched", "sock", "loutish", "veil", "table", "skillful", "dust", "smile", "taste", "didactic", "fire"]
word_bank = ["flex", "cars", "shin", "knee", "caps", "jazz", "crux", "buck", "lynx", "muck", "bell", "daze", "dojo", "bump", "waxy", "apex", "card", "bent", "mess", "hook", "wilt", "lock", "frog", "foxy", "milk", "film", "dead", "next"]
WORD = random.choice(word_bank)
letter_count = len(WORD)
print("\nWelcome to the cow game! I can't remember what it is called, but I sort of remember the rules. Basically, there is a random word chosen, and you have to guess. Correct letters are rings and correct letters in the correct spots are bullseyes. Enjoy!\n")
user_input = 0
# DIFFICULTY
while user_input == 0:
	print("How difficult do you want this to be?")
	print("Easy = 1, Normal = 2, Hard = 3, Nigh Impossible = 4, Impossible = 5")
	difficulty = input("Difficulty: ")
	if difficulty == "1":
		guesses = 30
		user_input = 1
		solved = 0
	else:
		if difficulty == "2":
			guesses = 20
			user_input = 1
			solved = 0
		else:
			if difficulty == "3":
				guesses = 13
				user_input = 1
				solved = 0
			else:
				if difficulty == "4":
					guesses = 1
					user_input = 1
					solved = 0
				else:
					if difficulty == "5":
						print("You lose!")
						solved = 1
						user_input = 1
						guesses = 0
					else:
						print("Please try again. \n")
						guesses = 0
						solved = 1
	if solved == 0:
		print("\nThe word has " + str(letter_count) + " characters. \n")
	while solved == 0:
		#Bulls and Ring Calculations
		if guesses >= 1:
			if guesses > 1:
				print("You have " + str(guesses) + " guesses left.")
			if guesses == 1:
				print("Last guess! Think carefully.")
			attempt = input("What is the password? ")
			rings = 0
			#Win
			if attempt == WORD:
				print("Congratulations! You win!")
				solved = 1
			#Not right yet
			else:
				bulls = 0
				print("Try again.")
				#Ring caclulations
				import re
				for i in WORD:
						if re.search(i, attempt):
								rings = rings + 1
				runs = len(attempt)
				#Bull Calculations
				while runs != 0:
					if runs >= letter_count:
						runs = runs - 1
					else:
						if WORD[runs-1] == attempt[runs-1]:
							bulls = bulls + 1
						runs = runs - 1
				#Debrief
				print("There are " + str(rings) + " rings and " + str(bulls) + " bulls. \n")
				guesses = guesses - 1
		else:
			solved = 1
#Lose message
if guesses == 0:
	print("The word was " + WORD + ". You lose. Wanna play again some other time?")
