import time
import random

from Helper import Geo_Questions
from Helper import History_Questions
from Helper import Science_Questions

Geo_points = 0
Geo_check = False

History_points = 0
History_check = False

SM_points = 0
SM_check = False


print("Welcome to the Academic Quiz Game!")

print("\n\n")

time.sleep(2)

name = input("Please tell me your name. ")
print(f"\nWelcome, {name.title()}! I hope you enjoy the game!")

time.sleep(1)

def choice_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	print("\n\n")

	choice = input(f"{name.title()}, would you like to [R]ead the rules or [S]kip? ")
	
	if choice.upper() == 'R':
		rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	if choice.upper() == 'S':
	  time.sleep(1)
	  options(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	else:
		print(f"\nPlease enter a valid option.")
		choice_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	
def rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.5)
	
	print("\nYou will be asked multiple choice questions about each of these categories: ")
	print("\n- U.S. and World Geography\n- U.S. and World History\n- Science/Math\n")
	
	time.sleep(2)
	print("\nAnswering correctly will give you a point and let you move on. If you answer incorrectly, you will have one more chance.")
	
	time.sleep(2)
	print("\n\nIf you get through all the questions, you will complete the category. Once you do this, you will be able to: ")

	print("\n- Move on to a different category\n- Practice the same category with randomly chosen questions\n- Quit the game\n")
	
	time.sleep(2)
	print("\nCompleting all the categories will cause the game to end. However, this game is not necessarilly about winning.")
	
	time.sleep(1.5)
	print("\nFinally, please DO NOT press any keys for no reason. Otherwise the game may crash.")
	time.sleep(1)
	after_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)


def Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	choice = input(f"\n\nAre you sure you want to quit the game? y/n ")
	
	if choice.lower() == 'y':
		print(f"\nThank you for playing the game. Exiting now...")
		time.sleep(1)
		exit(1)
	



def after_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.5)
	print("\n\n")
	choice = input(f"Enough with the rules. {name.title()}, are you ready to begin? y/n  ")
	if choice.lower() == 'y':
		print("\nSending you to the options menu...")
		options(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	elif choice.lower() == 'n':
  		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
  		after_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	else:
		print("\nPlease pick a valid option.")
		after_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		


def options(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):

	print("\n\n\nHere are the categories you can choose from: ")
	time.sleep(1)
	print("\n [1] U.S. and World Geography\n [2] U.S. and World History\n [3] Science/Math\n")


	choice = input("\nWhich category do you choose? [1], [2], or [3]  ")
	
	if choice == '1':
		print("\nSending you to U.S. and World Geography!")
		Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	elif choice == '2':
		print("\nSending you to U.S. and World History!")
		History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	elif choice == '3':
		print("\nSending you to Science/Math!")
		SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	else:
		print("\nPlease pick a valid option.")
		options(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	



def Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):

	if Geo_check and History_check and SM_check:
		conclusion(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	elif Geo_check and History_check and not SM_check:
		time.sleep(1.3)
		print(f"\nYou only have Science/Math left, sending you there now...")
		SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
			
	elif Geo_check and SM_check and not History_check:
		time.sleep(1.3)
		print(f"\nYou only have History left, sending you there now...")
		History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	

	elif History_check and SM_check and not Geo_check:
		time.sleep(1.3)
		print(f"\nYou only have Geography left, sending you there now...")
		Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	
	elif Geo_check and not SM_check and not History_check:
		time.sleep(1.3)
		choice = input("\nWould you like to go to [H]istory or [S]cience? ")
		
		if choice.upper() == 'H':
			print("\nSending you to U.S. and World History!")
			History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		elif choice.upper() == 'S':
			print("\nSending you to Science!")
			SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		else:
			print("\nPlease pick a valid option.")
			Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	
	elif History_check and not Geo_check and not SM_check:
		time.sleep(1.3)
		choice = input("\nWould you like to go to [G]eography or [S]cience and Math? ")
		
		if choice.upper() == 'G':
			print("\nSending you to U.S. and World Geography!")
			Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		elif choice.upper() == 'S':
			print("\nSending you to Science/Math!")
			SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		else:
			print("\nPlease pick a valid option.")
			Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	
	elif SM_check and not Geo_check and not History_check:
		time.sleep(1.3)
		choice = input("\nWould you like to go to [G]eography or [H]istory? ")
		
		if choice.upper() == 'G':
			print("\nSending you to U.S. and World Geography!")
			Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		elif choice.upper() == 'H':
			print("\nSending you to U.S. and World History!")
			History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		else:
			print("\nPlease pick a valid option.")
			Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)



def CheckScore(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	return f"\n{name.title()}, you have {Geo_points} geography points, {History_points} history points, and {SM_points} science/mathematics points."


		
def Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	time.sleep(1)
	print(f"\n\n\nWelcome to the Geography round!")
	time.sleep(1)
	print("\nYou will be given 3 questions, with 2 chances each. If you answer all 3 wrong, you will have to restart the category.")
	time.sleep(2)
	
	choice = input("\nWould you like to [P]roceed or [Q]uit? ")
	if choice.lower() == 'p':
		Geo_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	elif choice.lower() == 'q':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)

		
	else:
		print("\nPlease pick a valid option.")
		Geo_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)



def Geo_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	Official = Geo_Questions()
	
	Final3 = random.sample(Official, 3)
	Wrong_Questions = 0
	
	for i in range(3):
		question = Final3[i]
		
		time.sleep(1.5)
		print(f"\n\n\nHere is question {i+1}:\n")
		time.sleep(1)
		
		print(question['question'])
		time.sleep(1.3)
		print(question['choice'])
		response = input("  ")
		
		if response == (question['right_answer']):
			print("\nCorrect! Moving on to the next question...")
			Geo_points += 1
		
		if response != (question['right_answer']):
			print("\n\nTry again.")
			time.sleep(1)
			response1 = input(question['choice'] + "\n  ")
		
			if response1 == (question['right_answer']):
				print("\nCorrect! Moving on to the next question...")
				Geo_points += 1
		
			elif response1 != (question['right_answer']):
				print(f"\nIncorrect. The correct answer was {question['right_answer']}. Moving on to the next question...") 
				time.sleep(2)
				Wrong_Questions += 1
		
		if Wrong_Questions >= 3:
			print("\n\nUh oh! You answered 3 questions wrong, so you must start again. Sending you back to question 1...")
			time.sleep(2)
			Geo_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	time.sleep(1)	
	print("\n\nCongratulations, you have made it through the round WITHOUT incorrectly answering 3 questions!")
	
	Geo_check = True
	
	After_Geo(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)



def After_Geo(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.3)
	print("\n\n\nHere are your options:")
	print("\n [1] Move on to a different category\n [2] Practice the same category with randomly chosen questions\n [3] Check your score\n [4] Quit the game\n")
	
	choice = input("Which option do you choose? [1], [2], [3], or [4] ")
	
	if choice == "1":
		Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '2':
		print("\nSending you back to Geography!")
		Geo_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	elif choice == '3':
		print(CheckScore(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions))
		
		After_Geo(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '4':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		After_Geo(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	else:
		print("\nPlease pick a valid option.") 
		After_Geo(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		

def History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	time.sleep(1)
	print(f"\n\n\nWelcome to the History round!")
	time.sleep(1)

	print("\nYou will be given 3 questions, with 2 chances each. If you answer all 3 wrong, you will have to restart the category.")
	time.sleep(2)
	
	choice = input("\nWould you like to [P]roceed or [Q]uit? ")
	if choice.lower() == 'p':
		History_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	elif choice.lower() == 'q':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)


	else:
		print("\nPlease pick a valid option.")
		History_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)



def History_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	Official = History_Questions()
	
	Final3 = random.sample(Official, 3)
	Wrong_Questions = 0
	
	for i in range(3):
		question = Final3[i]
		
		time.sleep(1.5)
		print(f"\n\n\nHere is question {i+1}:\n")
		time.sleep(1)
		
		print(question['question'])
		time.sleep(1.3)
		print(question['choice'])
		response = input("  ")
		
		if response == (question['right_answer']):
			print("\nCorrect! Moving on to the next question...")
			History_points += 1
		
		if response != (question['right_answer']):
			print("\n\nTry again.")
			time.sleep(1)
			response1 = input(question['choice'] + "\n  ")
		
			if response1 == (question['right_answer']):
				print("\nCorrect! Moving on to the next question...")
				History_points += 1
		
			elif response1 != (question['right_answer']):
				print(f"\nIncorrect. The correct answer was {question['right_answer']}. Moving on to the next question...") 
				time.sleep(2)
				Wrong_Questions += 1
		
		if Wrong_Questions >= 3:
			print("\n\nUh oh! You answered 3 questions wrong, so you must start again. Sending you back to question 1...")
			time.sleep(2)
			History_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	time.sleep(1)	
	print("\n\nCongratulations, you have made it through the round WITHOUT incorrectly answering 3 questions!")
	
	History_check = True
	
	After_History(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)


	


def After_History(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.3)
	print("\n\n\nHere are your options:")
	print("\n [1] Move on to a different category\n [2] Practice the same category with randomly chosen questions\n [3] Check your score\n [4] Quit the game\n")
	
	choice = input("Which option do you choose? [1], [2], [3], or [4] ")
	
	if choice == "1":
		Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '2':
		print("\nSending you back to History!")
		History_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	elif choice == '3':
		print(CheckScore(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions))
		
		After_History(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '4':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		After_History(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	else:
		print("\nPlease pick a valid option.") 
		After_History(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		

def SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	time.sleep(1)
	print(f"\n\n\nWelcome to the Science round!")
	time.sleep(1)
	
	print("\nYou will be given 3 questions, with 2 chances each. If you answer all 3 wrong, you will have to restart the category.")
	time.sleep(2)
	
	choice = input("\nWould you like to [P]roceed or [Q]uit? ")
	if choice.lower() == 'p':
		SM_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
	
	elif choice.lower() == 'q':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)

  		
	else:
		print("\nPlease pick a valid option.")
		SM_Intro(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)


def SM_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	
	Official = Science_Questions()
	
	Final3 = random.sample(Official, 3)
	Wrong_Questions = 0
	
	for i in range(3):
		question = Final3[i]
		
		time.sleep(1.5)
		print(f"\n\n\nHere is question {i+1}:\n")
		time.sleep(1)
		
		print(question['question'])
		time.sleep(1.3)
		print(question['choice'])
		response = input("  ")
		
		if response == (question['right_answer']):
			print("\nCorrect! Moving on to the next question...")
			SM_points += 1
		
		if response != (question['right_answer']):
			print("\n\nTry again.")
			time.sleep(1)
			response1 = input(question['choice'] + "\n  ")
		
			if response1 == (question['right_answer']):
				print("\nCorrect! Moving on to the next question...")
				SM_points += 1
		
			elif response1 != (question['right_answer']):
				print(f"\nIncorrect. The correct answer was {question['right_answer']}. Moving on to the next question...") 
				time.sleep(2)
				Wrong_Questions += 1
		
		if Wrong_Questions >= 3:
			print("\n\nUh oh! You answered 3 questions wrong, so you must start again. Sending you back to question 1...")
			SM_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	time.sleep(1)
	print("\n\nCongratulations, you have made it through the round WITHOUT incorrectly answering 3 questions!")
	
	SM_check = True
	
	After_SM(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)


	


def After_SM(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.3)
	print("\n\n\nHere are your options:")
	print("\n [1] Move on to a different category\n [2] Practice the same category with randomly chosen questions\n [3] Check your score\n [4] Quit the game\n")
	
	choice = input("Which option do you choose? [1], [2], [3], or [4] ")
	
	if choice == "1":
		Switch(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '2':
		print("\nSending you back to Science!")
		SM_Main(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
			
	elif choice == '3':
		print(CheckScore(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions))
		After_SM(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
		
	elif choice == '4':
		Leave(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		After_SM(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
		
	else:
		print("\nPlease pick a valid option.") 
		After_SM(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)



def conclusion(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions):
	time.sleep(1.5)
	print("\n\n\nCongratulations! You have completed all three categories in the Academic Quiz Game!")
	
	time.sleep(1)
	print(f"\n{name.title()}, you scored {Geo_points} geography points, {History_points} history points, and {SM_points} science/mathematics points. Great job!")
	
	time.sleep(3)
	print("\nThank you for playing the game. If you want to play the game again, click the \"Run again\" button that will pop up in a few seconds.")
	time.sleep(3)


choice_rules(Geo_points, Geo_check, Geo_Questions, History_points, History_check, History_Questions, SM_points, SM_check, Science_Questions)
