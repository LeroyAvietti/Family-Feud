#Leroy & Ethan's CAT

#the variables and lists
import random 
global answer
answer = 0
global guess
guess = 0
global guesses
guesses = 3
global items
items = []
global rounds
rounds = 0
questions = ["", "fruit", "food"]

def game() :
  #an extra version of the global declorations to make sure its all working and setting down the items list and emptying it
  global rounds
  global items
  global guesses
  global guess
  global answer
  global questions
  items = []
  #setting the list size, words in the list, and the secret word picked from it along with the question asked
  words = int(input('How many words do you want to play with? '))
  question = random.choice(questions)
  if words == 1 :
    print(f"Name {words} {question}")
  else :
    print(f"Name {words} {question}s")
  for i in range(words): 
    inputs = input()
    items.append(inputs)
  secret_word = random.choice(items)
  print(secret_word)

  #round one begins, this begins the guessing segment, then the reveal of the secret wird and if you have one or lost. Then optionally beginning the game again if selected to do so
  rounds += 1
  print(f"Round {rounds}")
  print(items)
  guess = input(f"guess which {question} is the secret word ")
  while guess != secret_word:
    print("nup")
    guesses -= 1
    if guesses != 0:
      guess = input(f"guess which {question} is the secret word ")
    else:
      print("you lose")
      print(f"The secret word was {secret_word}")
      answer = input("play again? y/n")
  print("yep")
  answer = input("play again? y/n")
  if answer != 'y' :
    print('Thankyou for playing')
    exit()
  else:
    game()
game()