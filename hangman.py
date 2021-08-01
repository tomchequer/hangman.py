#This is a simples hangman game
#Enjoy
import random

possible_words = ['bottle', 'screen', 'knife', 'phone', 'water', 'computer', 'keyboard', 'person', 
'freedom', 'system', 'math', 'guitar', 'software', 'key', 'mouse', 'bag']

#possible_words = ['test', 'text']

randomword = possible_words[random.randint(0, (len(possible_words) - 1))]

print('Hello to my Hangman Game!')
print("This is your word!")

display = []

for i in randomword:
    display.append('_')

print(display)

userguess = input("\nPlease, guess a letter!\n").lower()

for i in range(len(randomword)):
    letter = randomword[i]
    if letter == userguess:
        display[i] = letter
        
print(display)

