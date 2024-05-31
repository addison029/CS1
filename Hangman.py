import random

HANGMAN_PICS = ['''
    +---+
       |
       |
       |
      ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
   O   |
   |   |
       |
       ===''', '''
    +---+
   O   |
  /|   |
       |
       ===''', '''
   +---+
   O   |
  /|\  |
       |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
      ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
      ===''']

words = ["hello", "world", "python","summer", "happy","love", "smart"]
secret = random.choice (words)

secret_list = list(secret)
hidden =[]
guesses = 0

for character in secret_list:
    hidden.append("_ ")
print("".join(hidden))

while "_ " in hidden and guesses < len(HANGMAN_PICS):
    print (HANGMAN_PICS[guesses])
    guess = input("Enter a letter: ")


    if guess in secret_list:
            for index in range(len(secret_list)):
                  if guess == secret_list[index]:
                    hidden[index] = guess
            print("".join(hidden))
    else:
        print("Letter not here!")
        guesses += 1
