import random
import time

#initial steps to invite in the game
print("Welcome to Hangman game\n")
name= input("Enter your name:")
print("hello" +name+ "! All the best!")
time.sleep(2)

print("\nThe game is about to start!\n Let's play Hangman!")
time.sleep(3)

def main():
	global count
	global display
	global word
	global already_guessed
	global length
	global play_game
	words_to_guess=["Wednesday", "Border", "Hera Pheri", "Jurassic Park", "Golmaal", "Aviator", "Ice Age", "Shrek", "Cars", "Madagascar", "Finding Nemo"]
	word= random.choice(words_to_guess)
	length= len(word)
	count= 0
	display= '_ '*length
	already_guessed=[]
	play_game=" "


#A loop to re-execute the game when the first round ends

def play_loop():
	global play_game
	play_game= input("Do you want to play again? Type Y for yes and N for no\n")
	while play_game not in ('y','n', 'Y', 'N'):
		play_game= input("Do you want to play again? Type Y for yes and N for no\n")
		if play_game== 'y' or 'Y':
			main()
		if play_game== 'n' or 'N':
			print("Thanks for playing! We expect you back again.\n")
			exit()


#Initializing all the conditions required for the game

def hangman():
	global count
	global display
	global word
	global already_guessed
	global play_game
	limit=5
	guess= input("This is the hangman word:" +display+ "Enter your guess: \n")
	guess=guess.strip()
	if len(guess.strip())==0 or len(guess.strip())>=2 or guess<= "9":
		print("Invalid input, Try a letter\n")
		hangman()

	elif guess in word:
		already_guessed.extend([guess])
		index=word.find(guess)
		word= word[:index] +guess+ display[index + 1:]
		display= display[:index] +guess+ display[index + 1:]
		print(display + "\n")

	elif guess in already_guessed:
		print("Try another letter.\n")

	else:
		count+=1

		if count==1:
			time.sleep(1)
			print("   _____\n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "  _|_   \n")
			print("Wrong guess." +str(limit-count)+ "guess remaining\n")

		elif count==2:
			time.sleep(1)
			print("   _____\n"
                  "   |   |\n"
                  "   |   |\n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "   |    \n"
                  "  _|_   \n")
			print("Wrong guess." +str(limit-count)+ "guess reamaining\n")

		elif count==3:
			time.sleep(3)
			print("   _____\n"
				  "   |   |\n"
				  "   |   |\n"
				  "   |   |\n"
				  "   |   0\n"
				  "   |    \n"
				  "   |    \n"
				  "   |    \n"
				  "  _|_   \n")
			print("Wrong guess." +str(limit-count)+ "Guess remaining.\n")

		elif count==4:
			time.sleep(4)
			print("   _____\n"
	    		  "   |   |\n"
	    		  "   |   |\n"
	    		  "   |   |\n"
	    		  "   |   0\n"
	    		  "   |  /|\ \n"
	    		  "   |  / \ \n"
	    		  "   |      \n"
	    		  "  _|_     \n")
			print("Wrong guess. You're hanged!!!\n")
			print("The word was:", already_guessed, word)
			play_loop()

    
	if word== ' '*length:
		print("Congrats!You have guessed the word correctly!\n")
		play_loop()

	elif count!=limit:
		hangman()

main()

hangman()	      	




