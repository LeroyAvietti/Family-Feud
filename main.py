#Leroy & Ethan's CATj
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
  global rounds
  global items
  global guesses
  global guess
  global answer
  global question
  items = []
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
      answer = input("play again? y/n")
  print("yep")
  answer = input("play again? y/n")
  if answer != 'y' :
    print('Thankyou for playing')
    exit()
  else:
    game()
game()