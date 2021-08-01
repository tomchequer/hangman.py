#This is a simples hangman game
#Enjoy
import random

possible_words = ['bottle', 'screen', 'knife', 'phone', 'water', 'computer', 'keyboard', 'person', 
'freedom', 'system', 'math', 'guitar', 'software', 'key', 'mouse', 'bag']
#possible_words = ['test', 'text']

randomword = possible_words[random.randint(0, (len(possible_words) - 1))]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

lives = 6

print('Hello, welcome to my Hangman Game!')
print(stages[lives])
print("This is your word!")

display = []
for i in randomword:
    display.append('_')

print(display)

end_of_game = False

while end_of_game == False: 
    
    userguess = input("\nPlease, guess a letter!\n").lower()

    for i in range(len(randomword)):
        letter = randomword[i]
        if letter == userguess:
            display[i] = letter
    
    if userguess not in randomword:
            lives -= 1   
            print(f'You have {lives} lives.')
            print(stages[lives])

    print(display)
    
    if '_' not in display:
        end_of_game = True
        print('You win!!!')
    elif lives == 0:
        end_of_game = True
        print('You loose.')



